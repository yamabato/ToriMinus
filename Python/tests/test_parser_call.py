from tori_test import *
from parser_test_util import *

# ---
# 関数呼び出しに関するテスト

def test_parser_CALL_01():
  expanded_code = get_expanded_code("f()")
  assert expanded_code == "CALL(VAR(f), ())" 

def test_parser_CALL_02():
  expanded_code = get_expanded_code("f(1)")
  assert expanded_code == "CALL(VAR(f), (INT(1)))" 

def test_parser_CALL_03():
  expanded_code = get_expanded_code("f(1, 2)")
  assert expanded_code == "CALL(VAR(f), (INT(1), INT(2)))" 

def test_parser_CALL_04():
  expanded_code = get_expanded_code("f(1, 2*2+3)")
  assert expanded_code == "CALL(VAR(f), (INT(1), ADD(MUL(INT(2), INT(2)), INT(3))))" 

def test_parser_CALL_05():
  expanded_code = get_expanded_code("f(1, g(a, b**2))")
  assert expanded_code == "CALL(VAR(f), (INT(1), CALL(VAR(g), (VAR(a), POWER(VAR(b), INT(2))))))" 

# ---
