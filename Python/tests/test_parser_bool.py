from tori_test import *
from parser_test_util import *

# ---
# 真偽値に関するテスト

def test_parser_BOOL_01():
  expanded_code = get_expanded_code("`true`;")
  assert expanded_code == "BOOL(true)" 

def test_parser_BOOL_02():
  expanded_code = get_expanded_code("`false`;")
  assert expanded_code == "BOOL(false)" 

def test_parser_BOOL_03():
  expanded_code = get_expanded_code("x = `false`;")
  assert expanded_code == "ASSIGN(VAR(x), BOOL(false))" 

# ---
