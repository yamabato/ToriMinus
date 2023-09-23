from tori_test import *
from lexer_test_util import *

# ---
# 識別子の字句解析に関するテスト

def test_lexer_IDENT_01():
  token_kind_list, token_value_list = get_tokens_info("a") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["a"] 

def test_lexer_IDENT_02():
  token_kind_list, token_value_list = get_tokens_info("abc") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["abc"] 

def test_lexer_IDENT_03():
  token_kind_list, token_value_list = get_tokens_info("_abc") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["_abc"] 

def test_lexer_IDENT_04():
  token_kind_list, token_value_list = get_tokens_info("a_bc") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["a_bc"] 

def test_lexer_IDENT_05():
  token_kind_list, token_value_list = get_tokens_info("abc123") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["abc123"] 

def test_lexer_IDENT_06():
  token_kind_list, token_value_list = get_tokens_info("abc_123") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["abc_123"] 

def test_lexer_IDENT_07():
  token_kind_list, token_value_list = get_tokens_info("abc_123 xxx") 
  assert token_kind_list == [TR_Token_Kind.IDENT, TR_Token_Kind.IDENT] 
  assert token_value_list == ["abc_123", "xxx"] 

def test_lexer_IDENT_08():
  token_kind_list, token_value_list = get_tokens_info("123abc") 
  assert token_kind_list == [TR_Token_Kind.INT, TR_Token_Kind.IDENT] 
  assert token_value_list == ["123", "abc"] 

def test_lexer_IDENT_09():
  token_kind_list, token_value_list = get_tokens_info("Abc") 
  assert token_kind_list == [TR_Token_Kind.IDENT] 
  assert token_value_list == ["Abc"] 

# ---

