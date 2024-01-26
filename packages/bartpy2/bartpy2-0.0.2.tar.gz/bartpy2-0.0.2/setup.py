from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
    name='bartpy2',
    version='0.0.2',
    description='Bayesian Additive Regression Trees for Python Updated in January 2024',
    url='https://github.com/abdulrehman1215/bartpy2',
    author='Abdul Rehman Raja',
    author_email='Abdul.rehman98455@gmail.com',
    install_requires=[
        'joblib',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'seaborn',
        'scikit-learn',
        'statsmodels',
        'tqdm',
    ]
)


