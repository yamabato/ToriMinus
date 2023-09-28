from tori_test import *
from eval_test_util import *

# ---
# 整数に関するテスト

def test_eval_INT_01():
  ret = run_tori_minus_test_code("1;")
  assert ret == 1

def test_eval_INT_02():
  ret = run_tori_minus_test_code("0;")
  assert ret == 0 

def test_eval_INT_03():
  ret = run_tori_minus_test_code("102;")
  assert ret == 102 

# ---
