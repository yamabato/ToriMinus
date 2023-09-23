from enum import IntEnum, auto

class TR_Token:
  def __init__(self, kind, value):
    self.kind = kind
    self.value = value


class TR_Token_Kind(IntEnum):
  INT = auto()
  DEC = auto()
  IDENT = auto()
  STRING = auto()
  PUNCT = auto()

class TR_Char_Type(IntEnum):
  WHITESPACE = auto()
  DIGIT = auto()
  IDENT = auto()
  DOUBLE_QUOT = auto()
  PUNCT_LETTER = auto()
