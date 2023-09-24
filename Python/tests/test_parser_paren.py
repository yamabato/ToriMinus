from tori_test import *
from parser_test_util import *

# ---
# 括弧に関するテスト

def test_parser_PAREN_01():
  expanded_code = get_expanded_code("(1+1)*2")
  assert expanded_code == "MUL(ADD(INT(1), INT(1)), INT(2))" 

def test_parser_PAREN_02():
  expanded_code = get_expanded_code("(-2)**2")
  assert expanded_code == "POWER(MINUS(INT(2)), INT(2))" 

def test_parser_PAREN_03():
  expanded_code = get_expanded_code("(f(1)+2)**2")
  assert expanded_code == "POWER(ADD(CALL(VAR(f), (INT(1))), INT(2)), INT(2))" 

# ---
