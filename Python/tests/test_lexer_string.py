from tori_test import *
from lexer_test_util import *

# ---
# 文字列の字句解析に関するテスト

def test_lexer_STRING_01():
  token_kind_list, token_value_list = get_tokens_info("\"a\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["a"] 

def test_lexer_STRING_02():
  token_kind_list, token_value_list = get_tokens_info("\"abc\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["abc"] 

def test_lexer_STRING_03():
  token_kind_list, token_value_list = get_tokens_info("\"123abc\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["123abc"] 

def test_lexer_STRING_04():
  token_kind_list, token_value_list = get_tokens_info("\"123 abc\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["123 abc"] 

def test_lexer_STRING_05():
  token_kind_list, token_value_list = get_tokens_info("\"123 \\nabc\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["123 \nabc"] 

def test_lexer_STRING_06():
  token_kind_list, token_value_list = get_tokens_info("\"\\\" aaaa \\\"\"") 
  assert token_kind_list == [TR_Token_Kind.STRING] 
  assert token_value_list == ["\" aaaa \""] 

# ---
