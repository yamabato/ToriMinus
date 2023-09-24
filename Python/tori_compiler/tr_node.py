from enum import IntEnum, auto

class TR_Node:
  kind = None
  
  left = None
  right = None

  value = None

class TR_Node_Kind(IntEnum):
  INT = auto()
  DEC = auto()

  ADD = auto()
  MUL = auto()

  MINUS = auto()
