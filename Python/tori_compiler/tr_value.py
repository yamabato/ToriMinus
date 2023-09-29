from enum import IntEnum, auto

class TR_Value:
  kind = None
  value = None
  
  args = None
  stmt = None

class TR_Value_Kind(IntEnum):
  num_ = auto()
  str_ = auto()
  bool_ = auto()
  non_ = auto()
