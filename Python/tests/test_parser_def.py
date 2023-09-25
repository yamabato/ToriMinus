from tori_test import *
from parser_test_util import *

# ---
# 関数定義に関するテスト

def test_parser_DEF_01():
  expanded_code = get_expanded_code("{()};")
  assert expanded_code == "DEF((), ())" 

def test_parser_DEF_02():
  expanded_code = get_expanded_code("{(arg1, arg2)};")
  assert expanded_code == "DEF((VAR(arg1), VAR(arg2)), ())" 

def test_parser_DEF_03():
  expanded_code = get_expanded_code("{(arg1, arg2), arg1+arg2};")
  assert expanded_code == "DEF((VAR(arg1), VAR(arg2)), (ADD(VAR(arg1), VAR(arg2))))" 

def test_parser_DEF_04():
  expanded_code = get_expanded_code("{(arg1, arg2), arg1+arg2, {(arg3), f(arg3)}};")
  assert expanded_code == "DEF((VAR(arg1), VAR(arg2)), (ADD(VAR(arg1), VAR(arg2)), DEF((VAR(arg3)), (CALL(VAR(f), (VAR(arg3)))))))" 

# ---
