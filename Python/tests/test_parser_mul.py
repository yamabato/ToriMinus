from tori_test import *
from parser_test_util import *

# ---
# 乗算に関するテスト

def test_parser_MUL_01():
  expanded_code = get_expanded_code("1*1;")
  assert expanded_code == "MUL(INT(1), INT(1))" 

def test_parser_MUL_02():
  expanded_code = get_expanded_code("1*2+3;")
  assert expanded_code == "ADD(MUL(INT(1), INT(2)), INT(3))" 

def test_parser_MUL_03():
  expanded_code = get_expanded_code("1+2*3;")
  assert expanded_code == "ADD(INT(1), MUL(INT(2), INT(3)))" 

# ---
