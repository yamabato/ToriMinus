from tori_test import *
from lexer_test_util import *

# ---
# 記号の字句解析に関するテスト

def test_lexer_PUNCT_01():
  token_kind_list, token_value_list = get_tokens_info("+ - * / % **") 
  assert token_kind_list == [TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT] 
  assert token_value_list == ["+", "-", "*", "/", "%", "**"] 

def test_lexer_PUNCT_02():
  token_kind_list, token_value_list = get_tokens_info("== != < > <= >=") 
  assert token_kind_list == [TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT] 
  assert token_value_list == ["==", "!=", "<", ">", "<=", ">="] 

def test_lexer_PUNCT_03():
  token_kind_list, token_value_list = get_tokens_info("= += -= *= /= %= **=") 
  assert token_kind_list == [TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT] 
  assert token_value_list == ["=", "+=", "-=", "*=", "/=", "%=", "**="] 

def test_lexer_PUNCT_04():
  token_kind_list, token_value_list = get_tokens_info("( ) { } , ;") 
  assert token_kind_list == [TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT, TR_Token_Kind.PUNCT] 
  assert token_value_list == ["(", ")", "{", "}", ",", ";"] 

# ---
