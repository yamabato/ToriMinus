from tori_test import *
from parser_test_util import *

# ---
# pyfuncの呼出に関するテスト

def test_parser_PYFUNC_CALL_01():
  expanded_code = get_expanded_code("#print();")
  assert expanded_code == "PYFUNC_CALL(#print, ())" 

def test_parser_PYFUNC_CALL_02():
  expanded_code = get_expanded_code("#print(1);")
  assert expanded_code == "PYFUNC_CALL(#print, (INT(1)))" 

def test_parser_PYFUNC_CALL_03():
  expanded_code = get_expanded_code("#print(1, 2, 3+#round(1.1));")
  assert expanded_code == "PYFUNC_CALL(#print, (INT(1), INT(2), ADD(INT(3), PYFUNC_CALL(#round, (DEC(1.1))))))" 

# ---
