from tori_test import *
from parser_test_util import *

# ---
# pyfuncに関するテスト

def test_parser_PYFUNC_01():
  expanded_code = get_expanded_code("pyfunc #print;")
  assert expanded_code == "PYFUNC(#print)" 

def test_parser_PYFUNC_02():
  expanded_code = get_expanded_code("pyfunc #print, #loop;")
  assert expanded_code == "PYFUNC(#print, #loop)" 

def test_parser_PYFUNC_03():
  expanded_code = get_expanded_code("pyfunc #print, #loop, #if;")
  assert expanded_code == "PYFUNC(#print, #loop, #if)" 

# ---
