from enum import IntEnum, auto

class TR_Node:
  kind = None
  
  left = None
  right = None

  value = None
  
  func = None 
  name = None
  args = None

  funcs = None

  exprs = None
  stmts = None
  if_stmts = None
  else_stmts = None

  init = None
  adv = None

class TR_Node_Kind(IntEnum):
  INT = auto()
  DEC = auto()
  STR = auto()
  BOOL = auto()
  NON = auto()
  VAR = auto()

  PYFUNC = auto()
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
  ASSIGN_AND = auto()
  ASSIGN_OR = auto()
  ASSIGN_XOR = auto()

  EQUAL = auto()
  NEQ = auto()
  LT = auto()
  GT = auto()
  LEQ = auto()
  GEQ = auto()

  ADD = auto()
  SUB = auto()
  MUL = auto()
  DIV = auto()
  MOD = auto()

  AND = auto()
  OR = auto()
  XOR = auto()
  NOT = auto()

  POW = auto()

  MINUS = auto()

  IF  = auto()
  WHILE = auto()
  FOR = auto()
