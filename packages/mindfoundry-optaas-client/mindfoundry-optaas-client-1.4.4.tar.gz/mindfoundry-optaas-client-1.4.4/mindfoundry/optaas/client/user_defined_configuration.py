from dataclasses import dataclass
from typing import Any, Dict, Optional

from mindfoundry.optaas.client.result import ScoreValueOrDict, VarianceValueOrDict, Result
from mindfoundry.optaas.client.configuration import Configuration

class _MockConfiguration(Configuration):
    """Used only internally, to post a result for a user-defined configuration."""

    def __init__(self):  # pylint: disable=super-init-not-called
        pass

@dataclass
class UserDefinedConfiguration:
    """ A user defined configuration containing the parameters values and optionally score,
        variance and user_defined_data."""
    values: Dict
    score: Optional[ScoreValueOrDict] = None
    variance: Optional[VarianceValueOrDict] = None
    user_defined_data: Any = None

    def get_body(self) -> Dict:
        body = {"values": self.values}
        if self.score is not None:
            result = Result(configuration=_MockConfiguration(), score=self.score, variance=self.variance,
                            user_defined_data=self.user_defined_data)
            body['results'] = [result.to_json_without_configuration()] # type: ignore
        return body
