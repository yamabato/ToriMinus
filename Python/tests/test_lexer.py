import os
import sys

sys.path.append(os.path.join(os.getcwd(), "tori_compiler/"))

from tr_lexer import tr_lexer
from tr_token import TR_Token, TR_Token_Kind

# ---
# ヘルパー関数類

def get_token_kind_list(tokens):
  token_kind_list = []
  for token in tokens:
    token_kind_list.append(token.kind)
  return token_kind_list

def get_token_value_list(tokens):
  token_value_list = []
  for token in tokens:
    token_value_list.append(token.value)
  return token_value_list

def get_tokens_info(program):
  tokens = tr_lexer(program) 
  token_kind_list = get_token_kind_list(tokens)
  token_value_list = get_token_value_list(tokens)
  
  return token_kind_list, token_value_list

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
