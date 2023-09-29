from tori_test import *
from eval_test_util import *

# ---
# 論理演算に関するテスト

def test_eval_LOGICAL_OPERATION_01():
  ret = run_tori_minus_test_code("!`true`;")
  assert not ret

def test_eval_LOGICAL_OPERATION_02():
  ret = run_tori_minus_test_code("`true` & `true`;")
  assert ret

def test_eval_LOGICAL_OPERATION_03():
  ret = run_tori_minus_test_code("`false` | `true`;")
  assert ret

def test_eval_LOGICAL_OPERATION_04():
  ret = run_tori_minus_test_code("`true` ^ `true`;")
  assert not ret

def test_eval_LOGICAL_OPERATION_05():
  ret = run_tori_minus_test_code("!`true` | `false`;")
  assert not ret

# ---
