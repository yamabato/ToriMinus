from tori_test import *
from parser_test_util import *

# ---
# 文字列に関するテスト

def test_parser_STR_01():
  expanded_code = get_expanded_code("\"abc\";")
  assert expanded_code == "STR(abc)" 

def test_parser_STR_02():
  expanded_code = get_expanded_code("\"abc\" + \"def\";")
  assert expanded_code == "ADD(STR(abc), STR(def))" 

def test_parser_STR_03():
  expanded_code = get_expanded_code("f(\"str\")")
  assert expanded_code == "CALL(VAR(f), (STR(str)))" 

def test_parser_STR_04():
  expanded_code = get_expanded_code("f(\"str\"*10)")
  assert expanded_code == "CALL(VAR(f), (MUL(STR(str), INT(10))))" 

# ---
