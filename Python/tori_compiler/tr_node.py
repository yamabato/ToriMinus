from enum import IntEnum, auto

class TR_Node:
  kind = None
  
  left = None
  right = None

  value = None
  
  func = None 
  name = None
  args = None

  exprs = None

class TR_Node_Kind(IntEnum):
  INT = auto()
  DEC = auto()
  VAR = auto()

  CALL = auto()
  DEF = auto()

  ASSIGN = auto()
  ASSIGN_ADD = auto()

  EQUAL = auto()

  ADD = auto()
  MUL = auto()

  POWER = auto()

  MINUS = auto()
