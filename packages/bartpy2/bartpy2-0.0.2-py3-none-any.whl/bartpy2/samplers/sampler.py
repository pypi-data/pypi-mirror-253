from abc import abstractmethod

from bartpy2.model import Model
from bartpy2.tree import Tree


class Sampler:

    @abstractmethod
    def step(self, model: Model, tree: Tree):
        raise NotImplementedError()