from tori_test import *
from parser_test_util import *

# ---
# その他の比較子に関するテスト

def test_parser_COMPARE_OTHER_01():
  expanded_code = get_expanded_code("a!=1")
  assert expanded_code == "NEQ(VAR(a), INT(1))" 

def test_parser_COMPARE_OTHER_02():
  expanded_code = get_expanded_code("a<1")
  assert expanded_code == "LT(VAR(a), INT(1))" 

def test_parser_COMPARE_OTHER_03():
  expanded_code = get_expanded_code("a>1")
  assert expanded_code == "GT(VAR(a), INT(1))" 

def test_parser_COMPARE_OTHER_04():
  expanded_code = get_expanded_code("a<=1")
  assert expanded_code == "LEQ(VAR(a), INT(1))" 

def test_parser_COMPARE_OTHER_05():
  expanded_code = get_expanded_code("a>=1")
  assert expanded_code == "GEQ(VAR(a), INT(1))" 

def test_parser_COMPARE_OTHER_06():
  expanded_code = get_expanded_code("a!=1+2")
  assert expanded_code == "NEQ(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_07():
  expanded_code = get_expanded_code("a<1+2")
  assert expanded_code == "LT(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_08():
  expanded_code = get_expanded_code("a>1+2")
  assert expanded_code == "GT(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_09():
  expanded_code = get_expanded_code("a<=1+2")
  assert expanded_code == "LEQ(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_10():
  expanded_code = get_expanded_code("a>=1+2")
  assert expanded_code == "GEQ(VAR(a), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_11():
  expanded_code = get_expanded_code("a+b!=1+2")
  assert expanded_code == "NEQ(ADD(VAR(a), VAR(b)), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_12():
  expanded_code = get_expanded_code("a+b<1+2")
  assert expanded_code == "LT(ADD(VAR(a), VAR(b)), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_13():
  expanded_code = get_expanded_code("a+b>1+2")
  assert expanded_code == "GT(ADD(VAR(a), VAR(b)), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_14():
  expanded_code = get_expanded_code("a+b<=1+2")
  assert expanded_code == "LEQ(ADD(VAR(a), VAR(b)), ADD(INT(1), INT(2)))" 

def test_parser_COMPARE_OTHER_15():
  expanded_code = get_expanded_code("a+b>=1+2")
  assert expanded_code == "GEQ(ADD(VAR(a), VAR(b)), ADD(INT(1), INT(2)))" 


# ---
