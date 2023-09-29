from tori_test import *
from lexer_test_util import *

#---
# nonの字句解析に関するテスト

def test_lexer_NON_01():
  token_kind_list, token_value_list = get_tokens_info("`non`") 
  assert token_kind_list == [TR_Token_Kind.NON] 
  assert token_value_list == ["non"] 

def test_lexer_NON_02():
  token_kind_list, token_value_list = get_tokens_info("x = `non`") 
  assert token_kind_list == [TR_Token_Kind.IDENT, TR_Token_Kind.PUNCT, TR_Token_Kind.NON] 
  assert token_value_list == ["x", "=", "non"] 

# ---
