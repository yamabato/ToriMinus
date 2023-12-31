from enum import IntEnum, auto

class TR_Token:
  def __init__(self, kind=None, value=None):
    self.kind = kind
    self.value = value


class TR_Token_Kind(IntEnum):
  INT = auto()
  DEC = auto()
  BOOL = auto()
  NON = auto()
  IDENT = auto()
  PYFUNC_IDENT = auto()
  STRING = auto()
  PUNCT = auto()

class TR_Char_Type(IntEnum):
  WHITESPACE = auto()
  DIGIT = auto()
  IDENT = auto()
  DOUBLE_QUOT = auto()
  PUNCT_LETTER = auto()
  COMMENT = auto()
  PYFUNC_PREFIX = auto()
  SP_VALUE_SIGN = auto()
