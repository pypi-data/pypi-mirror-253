from sklearn.decomposition import PCA as BasePCA

from mindfoundry.optaas.client.sklearn_pipelines.mixin import OptimizableBaseEstimator
from mindfoundry.optaas.client.sklearn_pipelines.parameter_maker import SklearnParameterMaker
from mindfoundry.optaas.client.sklearn_pipelines.utils import ParametersConstraintsAndPriorMeans


class PCA(BasePCA, OptimizableBaseEstimator):
    def make_parameters_constraints_and_prior_means(self, sk: SklearnParameterMaker, **kwargs)\
            -> ParametersConstraintsAndPriorMeans:
        """Generates :class:`Parameters <.Parameter>`, :class:`Constraints <.Constraint>`
         and :class:`PriorMeans <.PriorMeans>` to optimize a :class:`.PCA` estimator.

        Args:
            feature_count (int): Total number of features in your dataset.
        """

        feature_count = self.get_required_kwarg(kwargs, 'feature_count')
        max_n_components = feature_count - 1 if self.svd_solver == 'arpack' else feature_count

        return [
            sk.IntParameter('n_components', minimum=1, maximum=max_n_components),
            sk.BoolParameter('whiten')
        ], [], []
