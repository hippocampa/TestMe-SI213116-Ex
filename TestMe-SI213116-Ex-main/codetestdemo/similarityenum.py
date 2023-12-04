from enum import Enum


class Sim(Enum):
    """
    Strings similarities methods.

    """

    JARO_WRINKLER = 1
    LEVENSHTEIN = 2
