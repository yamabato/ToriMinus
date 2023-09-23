from tori_test import *
from lexer_test_util import *

# ---
# コメントに関するテスト

def test_lexer_COMMENT_01():
  token_kind_list, token_value_list = get_tokens_info("~~") 
  assert token_kind_list == [] 
  assert token_value_list == [] 

def test_lexer_COMMENT_02():
  token_kind_list, token_value_list = get_tokens_info("~comment~") 
  assert token_kind_list == [] 
  assert token_value_list == [] 

def test_lexer_COMMENT_03():
  token_kind_list, token_value_list = get_tokens_info("~a=1~") 
  assert token_kind_list == [] 
  assert token_value_list == [] 

def test_lexer_COMMENT_04():
  token_kind_list, token_value_list = get_tokens_info("1~a=1~") 
  assert token_kind_list == [TR_Token_Kind.INT] 
  assert token_value_list == ["1"] 

# ---
