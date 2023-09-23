from tori_test import *
from lexer_test_util import *

# ---
# 整数の字句解析に関するテスト

def test_lexer_INT_01():
  token_kind_list, token_value_list = get_tokens_info("1") 
  assert token_kind_list == [TR_Token_Kind.INT] 
  assert token_value_list == ["1"] 

def test_lexer_INT_02():
  token_kind_list, token_value_list = get_tokens_info("123") 
  assert token_kind_list == [TR_Token_Kind.INT] 
  assert token_value_list == ["123"] 

def test_lexer_INT_03():
  token_kind_list, token_value_list = get_tokens_info("0 987")
  assert token_kind_list == [TR_Token_Kind.INT, TR_Token_Kind.INT] 
  assert token_value_list == ["0", "987"] 

# ---

