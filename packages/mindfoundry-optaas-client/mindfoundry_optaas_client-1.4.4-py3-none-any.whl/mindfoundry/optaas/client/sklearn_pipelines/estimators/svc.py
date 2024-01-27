from sklearn.svm import SVC as BaseSVC, LinearSVC as BaseLinearSVC

from mindfoundry.optaas.client.parameter import Distribution
from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans, SMALLEST_NUMBER_ABOVE_ZERO


class _OptimizableSVC(OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize an SVC-based estimator."""

        parameters = [
            sk.FloatParameter('C', minimum=0.2, maximum=5.0, distribution=Distribution.LOGUNIFORM),
            sk.FloatParameter('tol', minimum=SMALLEST_NUMBER_ABOVE_ZERO, maximum=1),
            sk.ConstantParameter('class_weight', value='balanced', optional=True),
        ]

        return parameters, [], []


class SVC(BaseSVC, _OptimizableSVC):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize an :class:`.SVC` estimator."""

        parameters, constraints, prior_means = super().make_parameters_constraints_and_prior_means(sk, **kwargs)

        gamma_categories = ["scale"]
        if sk.defaults.get("gamma") == "auto_deprecated":
            sk.defaults["gamma"] = "scale"

        parameters.extend([
            sk.FloatOrCategorical('gamma', minimum=1.0e-5, maximum=1, categories=gamma_categories, distribution=Distribution.LOGUNIFORM),
            sk.CategoricalParameter('kernel', values=['linear', 'poly', 'rbf', 'sigmoid']),
            sk.IntParameter('degree', minimum=2, maximum=10, distribution=Distribution.LOGUNIFORM),
            sk.FloatParameter('coef0', minimum=0, maximum=1),
            sk.BoolParameter('shrinking')
        ])

        return parameters, constraints, prior_means


class LinearSVC(BaseLinearSVC, _OptimizableSVC):
    pass
