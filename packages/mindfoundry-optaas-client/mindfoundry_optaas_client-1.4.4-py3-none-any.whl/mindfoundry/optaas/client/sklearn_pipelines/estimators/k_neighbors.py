from sklearn.neighbors import KNeighborsClassifier as BaseKNeighborsClassifier, \
    KNeighborsRegressor as BaseKNeighborsRegressor

from mindfoundry.optaas.client.parameter import Distribution
from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans


class _OptimizableKNeighbors(OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize a KNeighbors estimator."""

        parameters = [
            sk.IntParameter('n_neighbors', minimum=1, maximum=20, distribution=Distribution.LOGUNIFORM),
            sk.CategoricalParameter('weights', values=["uniform", "distance"]),
            sk.CategoricalParameter('p', values=[1, 2]),
        ]

        return parameters, [], []


class KNeighborsClassifier(BaseKNeighborsClassifier, _OptimizableKNeighbors):
    """Allows us to optimize :class:`.KNeighborsClassifier` estimators."""


class KNeighborsRegressor(BaseKNeighborsRegressor, _OptimizableKNeighbors):
    """Allows us to optimize :class:`.KNeighborsRegressor` estimators."""
