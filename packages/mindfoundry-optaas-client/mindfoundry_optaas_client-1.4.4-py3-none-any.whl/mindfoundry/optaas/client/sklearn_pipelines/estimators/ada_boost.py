from sklearn.ensemble import AdaBoostClassifier as BaseAdaBoostClassifier, AdaBoostRegressor as BaseAdaBoostRegressor

from mindfoundry.optaas.client.parameter import Distribution
from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans


class _OptimizableAdaBoost(OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) \
            -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`,
        and :class:`PriorMeans <.PriorMeans>` to optimize an AdaBoost estimator."""

        return [
            sk.IntParameter('n_estimators', minimum=10, maximum=500),
            sk.FloatParameter('learning_rate', minimum=0.01, maximum=2.5, distribution=Distribution.LOGUNIFORM),
        ], [], []


class AdaBoostClassifier(BaseAdaBoostClassifier, _OptimizableAdaBoost):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) \
            -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`,
        and :class:`PriorMeans <.PriorMeans>` to optimize a :class:`.AdaBoostClassifier`."""

        parameters, constraints, prior_means = super().make_parameters_constraints_and_prior_means(sk, **kwargs)
        parameters.append(sk.CategoricalParameter('algorithm', values=['SAMME', 'SAMME.R']))
        return parameters, constraints, prior_means


class AdaBoostRegressor(BaseAdaBoostRegressor, _OptimizableAdaBoost):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs) \
            -> ParametersConstraintsAndPriorMeans:

        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`,
        and :class:`PriorMeans <.PriorMeans>` to optimize a :class:`.AdaBoostRegressor`."""

        parameters, constraints, prior_means = super().make_parameters_constraints_and_prior_means(sk, **kwargs)
        parameters.append(sk.CategoricalParameter('loss', values=['linear', 'square', 'exponential']))
        return parameters, constraints, prior_means
