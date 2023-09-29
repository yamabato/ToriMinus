from tori_test import *
from eval_test_util import *

# ---
# 真偽値に関するテスト

def test_eval_BOOL_01():
  ret = run_tori_minus_test_code("`true`;")
  assert ret == True

def test_eval_BOOL_02():
  ret = run_tori_minus_test_code("`false`;")
  assert ret == False

# ---
