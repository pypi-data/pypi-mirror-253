from sklearn.decomposition import FastICA as BaseICA

from mindfoundry.optaas.client.expressions import Constraint
from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans


class FastICA(BaseICA, OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs)\
            -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>` , :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize a :class:`.FastICA` estimator.

        Args:
            feature_count (int): Total number of features in your dataset.
        """

        feature_count = self.get_required_kwarg(kwargs, 'feature_count')
        fun = sk.CategoricalParameter('fun', values=["logcosh", "exp", "cube"])
        alpha = sk.FloatParameter('alpha', minimum=1, maximum=2, optional=True)

        parameters = [
            fun,
            sk.DictParameter('fun_args', items=[alpha]),
            sk.IntParameter('n_components', minimum=1, maximum=feature_count),
            sk.BoolParameter('whiten'),
            sk.CategoricalParameter('algorithm', values=['parallel', 'deflation'])
        ]

        constraints = [
            Constraint(when=fun != 'logcosh', then=alpha.is_absent()),
        ]

        return parameters, constraints, []
