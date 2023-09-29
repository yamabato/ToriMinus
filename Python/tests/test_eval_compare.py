from tori_test import *
from eval_test_util import *

# ---
# nonに関するテスト

def test_eval_COMPARE_01():
  ret = run_tori_minus_test_code("1 == 2;")
  assert not ret

def test_eval_COMPARE_02():
  ret = run_tori_minus_test_code("2 == 2;")
  assert ret

def test_eval_COMPARE_03():
  ret = run_tori_minus_test_code("2 != 2;")
  assert not ret

def test_eval_COMPARE_04():
  ret = run_tori_minus_test_code("21 != 2;")
  assert ret

def test_eval_COMPARE_05():
  ret = run_tori_minus_test_code("2 < 2;")
  assert not ret

def test_eval_COMPARE_06():
  ret = run_tori_minus_test_code("2 < 1;")
  assert not ret

def test_eval_COMPARE_07():
  ret = run_tori_minus_test_code("2 < 20;")
  assert ret

def test_eval_COMPARE_08():
  ret = run_tori_minus_test_code("20 > 2;")
  assert ret

def test_eval_COMPARE_09():
  ret = run_tori_minus_test_code("2 > 2;")
  assert not ret

def test_eval_COMPARE_10():
  ret = run_tori_minus_test_code("0 > 2;")
  assert not ret

def test_eval_COMPARE_11():
  ret = run_tori_minus_test_code("2 <= 2;")
  assert ret

def test_eval_COMPARE_12():
  ret = run_tori_minus_test_code("2 <= 5;")
  assert ret

def test_eval_COMPARE_13():
  ret = run_tori_minus_test_code("20 <= 5;")
  assert not ret

def test_eval_COMPARE_14():
  ret = run_tori_minus_test_code("20 >= 5;")
  assert ret

def test_eval_COMPARE_15():
  ret = run_tori_minus_test_code("20 >= 20;")
  assert ret

def test_eval_COMPARE_16():
  ret = run_tori_minus_test_code("2 >= 20;")
  assert not ret

def test_eval_COMPARE_17():
  ret = run_tori_minus_test_code("1 + 2 * 3 == (5 * 2**3 + (7 * 10**1 - 7) / 3 ** 2) % 8")
  assert ret 

# ---
