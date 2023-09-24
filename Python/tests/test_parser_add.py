from tori_test import *
from parser_test_util import *

# ---
# 加算に関するテスト

def test_parser_ADD_01():
  expanded_code = get_expanded_code("1+1")
  assert expanded_code == "ADD(INT(1), INT(1))" 

def test_parser_ADD_02():
  expanded_code = get_expanded_code("11+10")
  assert expanded_code == "ADD(INT(11), INT(10))" 

def test_parser_ADD_03():
  expanded_code = get_expanded_code("11+12+13")
  assert expanded_code == "ADD(ADD(INT(11), INT(12)), INT(13))" 

# ---
