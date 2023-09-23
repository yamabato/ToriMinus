from tori_test import *
from lexer_test_util import *

# ---
# PYFUNC識別子の字句解析に関するテスト

def test_lexer_PYFUNC_IDENT_01():
  token_kind_list, token_value_list = get_tokens_info("#loop") 
  assert token_kind_list == [TR_Token_Kind.PYFUNC_IDENT] 
  assert token_value_list == ["#loop"] 

def test_lexer_PYFUNC_IDENT_02():
  token_kind_list, token_value_list = get_tokens_info("#func1") 
  assert token_kind_list == [TR_Token_Kind.PYFUNC_IDENT] 
  assert token_value_list == ["#func1"] 

# ---
