from enum import IntEnum, auto

class Token:
  def __init__(self, kind, value):
    self.kind = kind
    self.value = value


class Token_Kind(IntEnum):
  INT = auto()
  DEC = auto()
