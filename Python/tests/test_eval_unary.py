from tori_test import *
from eval_test_util import *

# ---
# 代入演算子に関するテスト

def test_eval_UNARY_01():
  ret = run_tori_minus_test_code("+10;")
  assert ret == 10 

def test_eval_UNARY_02():
  ret = run_tori_minus_test_code("-10;")
  assert ret == -10 

def test_eval_UNARY_03():
  ret = run_tori_minus_test_code("-(10+2*3);")
  assert ret == -16 

def test_eval_UNARY_04():
  ret = run_tori_minus_test_code("a=12; -a;")
  assert ret == -12 

# ---
