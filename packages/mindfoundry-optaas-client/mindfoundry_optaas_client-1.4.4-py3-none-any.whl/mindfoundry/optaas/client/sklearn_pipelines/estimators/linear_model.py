from sklearn.linear_model import Lasso as BaseLasso, Ridge as BaseRidge

from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans, SMALLEST_NUMBER_ABOVE_ZERO


class _OptimizableLinearModel(OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs)\
            -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize a linear model."""

        return [sk.FloatParameter('alpha', minimum=SMALLEST_NUMBER_ABOVE_ZERO, maximum=1)], [], []


class Lasso(BaseLasso, _OptimizableLinearModel):
    """Allows us to optimize a :class:`.Lasso` estimator."""


class Ridge(BaseRidge, _OptimizableLinearModel):
    """Allows us to optimize a :class:`.Ridge` estimator."""
