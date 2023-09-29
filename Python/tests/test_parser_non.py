from tori_test import *
from parser_test_util import *

# ---
# nonに関するテスト

def test_parser_NON_01():
  expanded_code = get_expanded_code("`non`;")
  assert expanded_code == "NON(non)" 

def test_parser_NON_02():
  expanded_code = get_expanded_code("x = `non`;")
  assert expanded_code == "ASSIGN(VAR(x), NON(non))" 

# ---
