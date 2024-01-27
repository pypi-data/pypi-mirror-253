from enum import Enum


class Goal(Enum):
    """Specifies whether OPTaaS will aim for the lowest (min) or highest (max) score"""
    min = 0  # pylint: disable=invalid-name
    max = 1  # pylint: disable=invalid-name
