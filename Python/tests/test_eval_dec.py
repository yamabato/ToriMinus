from tori_test import *
from eval_test_util import *

# ---
# 小数に関するテスト

def test_eval_DEC_01():
  ret = run_tori_minus_test_code("1.0;")
  assert ret == 1.0

def test_eval_DEC_02():
  ret = run_tori_minus_test_code(".5;")
  assert ret == 0.5 

def test_eval_DEC_03():
  ret = run_tori_minus_test_code("12.;")
  assert ret == 12.0 

# ---
