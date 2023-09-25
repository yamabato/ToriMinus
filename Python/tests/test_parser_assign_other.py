from tori_test import *
from parser_test_util import *

# ---
# 代入のその他演算子に関するテスト

def test_parser_ASSIGN_OTHER_01():
  expanded_code = get_expanded_code("a+=1")
  assert expanded_code == "ASSIGN_ADD(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_02():
  expanded_code = get_expanded_code("a-=1")
  assert expanded_code == "ASSIGN_SUB(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_03():
  expanded_code = get_expanded_code("a*=1")
  assert expanded_code == "ASSIGN_MUL(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_04():
  expanded_code = get_expanded_code("a/=1")
  assert expanded_code == "ASSIGN_DIV(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_05():
  expanded_code = get_expanded_code("a%=1")
  assert expanded_code == "ASSIGN_MOD(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_06():
  expanded_code = get_expanded_code("a**=1")
  assert expanded_code == "ASSIGN_POW(VAR(a), INT(1))" 

def test_parser_ASSIGN_OTHER_07():
  expanded_code = get_expanded_code("a+=1+2")
  assert expanded_code == "ASSIGN_ADD(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_08():
  expanded_code = get_expanded_code("a-=1+2")
  assert expanded_code == "ASSIGN_SUB(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_09():
  expanded_code = get_expanded_code("a*=1+2")
  assert expanded_code == "ASSIGN_MUL(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_10():
  expanded_code = get_expanded_code("a/=1+2")
  assert expanded_code == "ASSIGN_DIV(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_11():
  expanded_code = get_expanded_code("a%=1+2")
  assert expanded_code == "ASSIGN_MOD(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_12():
  expanded_code = get_expanded_code("a**=1+2")
  assert expanded_code == "ASSIGN_POW(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_ASSIGN_OTHER_07():
  expanded_code = get_expanded_code("a+=1+2")
  assert expanded_code == "ASSIGN_ADD(VAR(a), ADD(INT(1), INT(2)))" 

# ---
