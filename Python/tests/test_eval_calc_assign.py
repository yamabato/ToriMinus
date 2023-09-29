from tori_test import *
from eval_test_util import *

# ---
# 代入演算子に関するテスト

def test_eval_CALC_ASSIGN_01():
  ret = run_tori_minus_test_code("a=10; a+=5;")
  assert ret == 15 

def test_eval_CALC_ASSIGN_02():
  ret = run_tori_minus_test_code("a=10; a-=5;")
  assert ret == 5 

def test_eval_CALC_ASSIGN_03():
  ret = run_tori_minus_test_code("a=10; a*=5;")
  assert ret == 50 

def test_eval_CALC_ASSIGN_04():
  ret = run_tori_minus_test_code("a=10; a/=5;")
  assert ret == 2.0 

def test_eval_CALC_ASSIGN_05():
  ret = run_tori_minus_test_code("a=10; a%=5;")
  assert ret == 0 

def test_eval_CALC_ASSIGN_06():
  ret = run_tori_minus_test_code("a=10; a**=5;")
  assert ret == 100000 

# ---
