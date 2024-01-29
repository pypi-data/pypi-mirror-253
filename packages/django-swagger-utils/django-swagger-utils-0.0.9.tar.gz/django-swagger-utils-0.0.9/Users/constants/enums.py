from enum import Enum

# from ib_common.constants import BaseEnumClass


class CodeLanguage(Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"


class ReactionType(Enum):
    LIKE = "LIKE"
    WOW = "WOW"
    HAHA = "HAHA"
    DISLIKE = "DISLIKE"
    SAD = "SAD"
    ANGRY = "ANGRY"