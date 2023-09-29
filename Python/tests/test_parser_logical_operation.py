from tori_test import *
from parser_test_util import *

# ---
# 論理演算に関するテスト

def test_parser_LOGICAL_OPERATION_01():
  expanded_code = get_expanded_code("`true` & `false`;")
  assert expanded_code == "AND(BOOL(true), BOOL(false))" 

def test_parser_LOGICAL_OPERATION_02():
  expanded_code = get_expanded_code("`true` | `false`;")
  assert expanded_code == "OR(BOOL(true), BOOL(false))" 

def test_parser_LOGICAL_OPERATION_04():
  expanded_code = get_expanded_code("`true` ^ `false`;")
  assert expanded_code == "XOR(BOOL(true), BOOL(false))" 

def test_parser_LOGICAL_OPERATION_05():
  expanded_code = get_expanded_code("!`true`;")
  assert expanded_code == "NOT(BOOL(true))" 

def test_parser_LOGICAL_OPERATION_06():
  expanded_code = get_expanded_code("!`true` | `false`;")
  assert expanded_code == "OR(NOT(BOOL(true)), BOOL(false))" 

# ---
