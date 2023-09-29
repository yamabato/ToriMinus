from tori_test import *
from eval_test_util import *

# ---
# nonに関するテスト

def test_eval_NON_01():
  ret = run_tori_minus_test_code("`non`;")
  assert ret == None

def test_eval_NON_02():
  ret = run_tori_minus_test_code("x = `non`;")
  assert ret == None

# ---
