from tori_test import *
from eval_test_util import *

# ---
# 関数に関するテスト

def test_eval_FUNC_01():
  ret = run_tori_minus_test_code("{(a, b), a+b}(1, 2);")
  assert ret == 3

def test_eval_FUNC_02():
  ret = run_tori_minus_test_code("{(), 10*2};")
  assert ret == 20 

def test_eval_FUNC_03():
  ret = run_tori_minus_test_code("{(), };")
  assert ret == None

def test_eval_FUNC_04():
  ret = run_tori_minus_test_code("f = {(x, y), x**y};f(2, 8)")
  assert ret == 256

def test_eval_FUNC_05():
  ret = run_tori_minus_test_code("f = {(g), g()};g = {(), 10};f(g);")
  assert ret == 10 

# ---
