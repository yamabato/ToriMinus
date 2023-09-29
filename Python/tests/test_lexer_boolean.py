from tori_test import *
from lexer_test_util import *

#---
# 真偽値の字句解析に関するテスト

def test_lexer_BOOL_01():
  token_kind_list, token_value_list = get_tokens_info("`true`") 
  assert token_kind_list == [TR_Token_Kind.BOOL] 
  assert token_value_list == ["true"] 

def test_lexer_BOOL_02():
  token_kind_list, token_value_list = get_tokens_info("`false`") 
  assert token_kind_list == [TR_Token_Kind.BOOL] 
  assert token_value_list == ["false"] 

def test_lexer_BOOL_03():
  token_kind_list, token_value_list = get_tokens_info("b = `true`") 
  assert token_kind_list == [TR_Token_Kind.IDENT, TR_Token_Kind.PUNCT, TR_Token_Kind.BOOL] 
  assert token_value_list == ["b", "=", "true"] 

# ---
