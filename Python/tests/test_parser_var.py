from tori_test import *
from parser_test_util import *

# ---
# 変数に関するテスト

def test_parser_VAR_01():
  expanded_code = get_expanded_code("a;")
  assert expanded_code == "VAR(a)" 

def test_parser_VAR_02():
  expanded_code = get_expanded_code("a+b;")
  assert expanded_code == "ADD(VAR(a), VAR(b))" 

def test_parser_VAR_03():
  expanded_code = get_expanded_code("-a+b;")
  assert expanded_code == "ADD(MINUS(VAR(a)), VAR(b))" 

def test_parser_VAR_04():
  expanded_code = get_expanded_code("1+-a+b;")
  assert expanded_code == "ADD(ADD(INT(1), MINUS(VAR(a))), VAR(b))" 

# ---
