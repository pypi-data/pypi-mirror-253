from typing import List

from joblib import Parallel, delayed
import numpy as np
import pandas as pd
from sklearn.base import RegressorMixin, BaseEstimator

from bartpy2.model import Model
from bartpy2.data import Data
from bartpy2.samplers.schedule import SampleSchedule
from bartpy2.samplers.modelsampler import ModelSampler
from bartpy2.sigma import Sigma
from bartpy2.samplers.treemutation.uniform.likihoodratio import UniformTreeMutationLikihoodRatio
from bartpy2.samplers.treemutation.uniform.proposer import UniformMutationProposer
from bartpy2.samplers.treemutation.treemutation import TreeMutationSampler
from bartpy2.samplers.sigma import SigmaSampler
from bartpy2.samplers.leafnode import LeafNodeSampler


class SklearnModel(BaseEstimator, RegressorMixin):
    """
    The main access point to building BART models in bartpy2

    Parameters
    ----------
    n_trees: int
        the number of trees to use, more trees will make a smoother fit, but slow training and fitting
    n_chains: int
        the number of independent chains to run
        more chains will improve the quality of the samples, but will require more computation
    sigma_a: float
        shape parameter of the prior on sigma
    sigma_b: float
        scale parameter of the prior on sigma
    n_samples: int
        how many recorded samples to take
    n_burn: int
        how many samples to run without recording to reach convergence
    thin: float
        percentage of samples to store.
        use this to save memory when running large models
    p_grow: float
        probability of choosing a grow mutation in tree mutation sampling
    p_prune: float
        probability of choosing a prune mutation in tree mutation sampling
    alpha: float
        prior parameter on tree structure
    beta: float
        prior parameter on tree structure
    store_in_sample_predictions: bool
        whether to store full prediction samples
        set to False if you don't need in sample results - saves a lot of memory
    n_jobs: int
        how many cores to use when computing MCMC samples
    """

    def __init__(self,
                 n_trees: int=50,
                 n_chains: int=4,
                 sigma_a: float=0.001,
                 sigma_b: float=0.001,
                 n_samples: int=200,
                 n_burn: int=200,
                 thin: float=0.1,
                 p_grow: float=0.5,
                 p_prune: float=0.5,
                 alpha: float=0.95,
                 beta: float=2.,
                 store_in_sample_predictions: bool=True,
                 n_jobs=4):
        self.n_trees = n_trees
        self.n_chains = n_chains
        self.sigma_a = sigma_a
        self.sigma_b = sigma_b
        self.n_burn = n_burn
        self.n_samples = n_samples
        self.p_grow = p_grow
        self.p_prune = p_prune
        self.alpha = alpha
        self.beta = beta
        self.thin = thin
        self.n_jobs = n_jobs
        self.store_in_sample_predictions = store_in_sample_predictions
        self.sigma, self.data, self.model, self.proposer, self.likihood_ratio, self.sampler, self._prediction_samples, self._model_samples, self.schedule = [None] * 9

    def fit(self, X: pd.DataFrame, y: np.ndarray) -> 'SklearnModel':
        """
        Learn the model based on training data

        Parameters
        ----------
        X: pd.DataFrame
            training covariates
        y: np.ndarray
            training targets

        Returns
        -------
        SklearnModel
            self with trained parameter values
        """
        from copy import deepcopy
        if type(X) == pd.DataFrame:
            X = X.values

        self.data = Data(deepcopy(X), deepcopy(y), normalize=True)
        self.sigma = Sigma(self.sigma_a, self.sigma_b, self.data.normalizing_scale)
        self.model = Model(self.data, self.sigma, n_trees=self.n_trees, alpha=self.alpha, beta=self.beta)
        self.proposer = UniformMutationProposer([self.p_grow, self.p_prune])
        self.likihood_ratio = UniformTreeMutationLikihoodRatio([self.p_grow, self.p_prune])
        self.tree_sampler = TreeMutationSampler(self.proposer, self.likihood_ratio)
        self.schedule = SampleSchedule(self.tree_sampler, LeafNodeSampler(), SigmaSampler())
        self.sampler = ModelSampler(self.schedule)

        def sample_thread(sampler, model, n_samples, n_burn, thin, store_in_sample_predictions):
            return Parallel(n_jobs=self.n_jobs)(delayed(sampler.samples)(model, n_samples, n_burn, thin, store_in_sample_predictions) for x in range(self.n_chains))
        self.extract = sample_thread(self.sampler, self.model, self.n_samples, self.n_burn, thin = self.thin, store_in_sample_predictions = self.store_in_sample_predictions)

        self._model_samples, self._prediction_samples = self.extract[0]
        for x in self.extract[1:]:
            self._model_samples += x[0]
            self._prediction_samples = np.concatenate([self._prediction_samples, x[1]], axis=0)
        return self

    def predict(self, X: np.ndarray=None):
        """
        Predict the target corresponding to the provided covariate matrix
        If X is None, will predict based on training covariates

        Prediction is based on the mean of all samples

        Parameters
        ----------
        X: pd.DataFrame
            covariates to predict from

        Returns
        -------
        np.ndarray
            predictions for the X covariates
        """
        if X is None:
            return self.data.unnormalize_y(self._prediction_samples.mean(axis=0))
        else:
            return self._out_of_sample_predict(X)

    def _out_of_sample_predict(self, X):
        return self.data.unnormalize_y(np.mean([x.predict(X) for x in self._model_samples], axis=0))

    def fit_predict(self, X, y):
        self.fit(X, y)
        return self.predict()

    @property
    def model_samples(self) -> List[Model]:
        """
        Array of the model as it was after each sample.
        Useful for examining for:

         - examining the state of trees, nodes and sigma throughout the sampling
         - out of sample prediction

        Returns None if the model hasn't been fit

        Returns
        -------
        List[Model]
        """
        return self._model_samples

    @property
    def prediction_samples(self):
        """
        Matrix of prediction samples at each point in sampling
        Useful for assessing convergence, calculating point estimates etc.

        Returns
        -------
        np.ndarray
            prediction samples with dimensionality n_samples * n_points
        """
        return self.prediction_samples