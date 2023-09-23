from tori_test import *

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
