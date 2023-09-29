from tori_test import *
from eval_test_util import *

# ---
# 文字列に関するテスト

def test_eval_STR_01():
  ret = run_tori_minus_test_code("\"str\";")
  assert ret == "str" 

def test_eval_STR_02():
  ret = run_tori_minus_test_code("\"str\" + \"aaa\";")
  assert ret == "straaa"

def test_eval_STR_03():
  ret = run_tori_minus_test_code("\"str\" * 12;")
  assert ret == "strstrstrstrstrstrstrstrstrstrstrstr"

# ---
