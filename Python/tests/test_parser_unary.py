from tori_test import *
from parser_test_util import *

# ---
# 単項演算子に関するテスト

def test_parser_UNARY_01():
  expanded_code = get_expanded_code("+1")
  assert expanded_code == "INT(1)" 

def test_parser_UNARY_02():
  expanded_code = get_expanded_code("-1")
  assert expanded_code == "MINUS(INT(1))" 

def test_parser_UNARY_03():
  expanded_code = get_expanded_code("+10")
  assert expanded_code == "INT(10)" 

def test_parser_UNARY_04():
  expanded_code = get_expanded_code("-10")
  assert expanded_code == "MINUS(INT(10))" 

# ---
