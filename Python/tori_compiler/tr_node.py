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
  STR = auto()
  VAR = auto()

  CALL = auto()
  PYFUNC_CALL = auto()
  DEF = auto()

  ASSIGN = auto()
  ASSIGN_ADD = auto()
  ASSIGN_SUB = auto()
  ASSIGN_MUL = auto()
  ASSIGN_DIV = auto()
  ASSIGN_MOD = auto()
  ASSIGN_POW = auto()

  EQUAL = auto()
  NEQ = auto()
  LT = auto()
  GT = auto()
  LEQ = auto()
  GEQ = auto()

  ADD = auto()
  MUL = auto()

  POWER = auto()

  MINUS = auto()
