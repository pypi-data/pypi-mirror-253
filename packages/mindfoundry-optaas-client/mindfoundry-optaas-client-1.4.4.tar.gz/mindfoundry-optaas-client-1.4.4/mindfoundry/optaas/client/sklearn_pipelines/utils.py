import warnings
from abc import ABC, abstractmethod
from typing import List, Union, Tuple

from numpy import nextafter
from sklearn.base import BaseEstimator

from mindfoundry.optaas.client.expressions import Constraint, PriorMeanExpression
from mindfoundry.optaas.client.parameter import GroupParameter, Parameter

SMALLEST_NUMBER_ABOVE_ZERO = nextafter(0.0, 1)
LARGEST_NUMBER_BELOW_ONE = nextafter(1.0, 0)

ParametersConstraintsAndPriorMeans = Tuple[List[Parameter], List[Constraint], List[PriorMeanExpression]]


class Optimizable(ABC):
    """Superclass for all optimizable steps."""

    @abstractmethod
    def make_all_parameters_constraints_and_prior_means(self, estimator_name: str, id_prefix: str,
                                                        **kwargs) -> ParametersConstraintsAndPriorMeans:
        """Returns all parameters, constraints, and prior Means for multiple estimators in a group or choice."""


Estimator = Union[BaseEstimator, Optimizable]
EstimatorTuple = Tuple[str, Estimator]


def _get_all_parameters_and_constraints_and_prior_means(estimators: List[EstimatorTuple], id_prefix: str,
                                                        **kwargs) -> ParametersConstraintsAndPriorMeans:
    all_parameters = []
    all_constraints = []
    all_prior_means = []

    for estimator_name, estimator in estimators:
        if isinstance(estimator, Optimizable):
            parameters, constraints, prior_means\
                = estimator.make_all_parameters_constraints_and_prior_means(estimator_name, id_prefix, **kwargs)
        else:
            warnings.warn(f"{type(estimator).__name__} is not an Optimizable estimator.")
            parameters = [GroupParameter(estimator_name, id=_make_id(id_prefix + estimator_name), items=[])]
            constraints = []
            prior_means = []

        all_parameters.extend(parameters)
        all_constraints.extend(constraints)
        all_prior_means.extend(prior_means)

    return all_parameters, all_constraints, all_prior_means


def _make_id(estimator_name: str) -> str:
    return estimator_name.replace(' ', '-')


class MissingArgumentError(ValueError):
    """Raised when a required argument is missing from kwargs in :meth:`.OPTaaSClient.create_sklearn_task`"""

    def __init__(self, required_arg: str, estimator) -> None:
        super().__init__(f"{required_arg} is required in kwargs in order to optimize {type(estimator).__name__}")
