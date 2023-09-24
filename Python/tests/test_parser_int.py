from tori_test import *
from parser_test_util import *

# ---
# 整数に関するテスト

def test_parser_INT_01():
  expanded_code = get_expanded_code("1")
  assert expanded_code == "INT(1)" 

def test_parser_INT_02():
  expanded_code = get_expanded_code("10")
  assert expanded_code == "INT(10)" 

# ---
