from tori_test import *
from parser_test_util import *

# ---
# 累乗に関するテスト

def test_parser_POWER_01():
  expanded_code = get_expanded_code("2**2")
  assert expanded_code == "POWER(INT(2), INT(2))" 

def test_parser_POWER_02():
  expanded_code = get_expanded_code("-2**2")
  assert expanded_code == "MINUS(POWER(INT(2), INT(2)))" 

def test_parser_POWER_03():
  expanded_code = get_expanded_code("-2**2*5")
  assert expanded_code == "MUL(MINUS(POWER(INT(2), INT(2))), INT(5))" 

def test_parser_POWER_04():
  expanded_code = get_expanded_code("5+-2**2")
  assert expanded_code == "ADD(INT(5), MINUS(POWER(INT(2), INT(2))))" 

# ---
