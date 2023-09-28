from tori_test import *
from eval_test_util import *

# ---
# 算術演算に関するテスト

def test_eval_CALC_01():
  ret = run_tori_minus_test_code("1+2;")
  assert ret == 3

def test_eval_CALC_02():
  ret = run_tori_minus_test_code("1+2*3;")
  assert ret == 7

def test_eval_CALC_03():
  ret = run_tori_minus_test_code("(1+2)*3;")
  assert ret == 9

def test_eval_CALC_04():
  ret = run_tori_minus_test_code("5*10;")
  assert ret == 50

def test_eval_CALC_05():
  ret = run_tori_minus_test_code("10/2;")
  assert ret == 5

def test_eval_CALC_06():
  ret = run_tori_minus_test_code("5%2;")
  assert ret == 1

def test_eval_CALC_07():
  ret = run_tori_minus_test_code("(10**2/20)*2%3;")
  assert ret == 1

# ---
