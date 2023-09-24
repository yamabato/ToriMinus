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

def test_parser_UNARY_05():
  expanded_code = get_expanded_code("1 + -10")
  assert expanded_code == "ADD(INT(1), MINUS(INT(10)))" 

def test_parser_UNARY_06():
  expanded_code = get_expanded_code("+11 + -10")
  assert expanded_code == "ADD(INT(11), MINUS(INT(10)))" 

def test_parser_UNARY_07():
  expanded_code = get_expanded_code("-11 + -10 + -12")
  assert expanded_code == "ADD(ADD(MINUS(INT(11)), MINUS(INT(10))), MINUS(INT(12)))" 

# ---
