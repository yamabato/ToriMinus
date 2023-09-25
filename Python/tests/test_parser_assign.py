from tori_test import *
from parser_test_util import *

# ---
# 代入に関するテスト

def test_parser_ASSIGN_01():
  expanded_code = get_expanded_code("a=1;")
  assert expanded_code == "ASSIGN(VAR(a), INT(1))" 

def test_parser_ASSIGN_02():
  expanded_code = get_expanded_code("a=1+2*3;")
  assert expanded_code == "ASSIGN(VAR(a), ADD(INT(1), MUL(INT(2), INT(3))))" 

def test_parser_ASSIGN_03():
  expanded_code = get_expanded_code("a=b=2+3;")
  assert expanded_code == "ASSIGN(VAR(a), ASSIGN(VAR(b), ADD(INT(2), INT(3))))" 

# ---
