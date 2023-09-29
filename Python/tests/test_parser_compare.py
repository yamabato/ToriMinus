from tori_test import *
from parser_test_util import *

# ---
# 比較に関するテスト

def test_parser_EQUAL_01():
  expanded_code = get_expanded_code("a==1;")
  assert expanded_code == "EQUAL(VAR(a), INT(1))" 

def test_parser_EQUAL_02():
  expanded_code = get_expanded_code("a==1+2;")
  assert expanded_code == "EQUAL(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_EQUAL_03():
  expanded_code = get_expanded_code("a**2==1+2;")
  assert expanded_code == "EQUAL(POW(VAR(a), INT(2)), ADD(INT(1), INT(2)))" 

# ---
