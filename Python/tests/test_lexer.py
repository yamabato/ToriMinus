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
# 小数の字句解析に関するテスト

def test_lexer_DEC_01():
  token_kind_list, token_value_list = get_tokens_info("1.0") 
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == ["1.0"] 

def test_lexer_DEC_02():
  token_kind_list, token_value_list = get_tokens_info("1.") 
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == ["1."] 
  
def test_lexer_DEC_03():
  token_kind_list, token_value_list = get_tokens_info(".1") 
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == [".1"] 
  
def test_lexer_DEC_04():
  token_kind_list, token_value_list = get_tokens_info("123.45") 
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == ["123.45"] 
  
def test_lexer_DEC_05():
  token_kind_list, token_value_list = get_tokens_info("123.") 
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == ["123."] 
  
def test_lexer_DEC_06():
  token_kind_list, token_value_list = get_tokens_info(".987")
  assert token_kind_list == [TR_Token_Kind.DEC] 
  assert token_value_list == [".987"] 
  
def test_lexer_DEC_06():
  token_kind_list, token_value_list = get_tokens_info("12. .987")
  assert token_kind_list == [TR_Token_Kind.DEC, TR_Token_Kind.DEC] 
  assert token_value_list == ["12.", ".987"] 
  
def test_lexer_DEC_07():
  token_kind_list, token_value_list = get_tokens_info("12.3 .987")
  assert token_kind_list == [TR_Token_Kind.DEC, TR_Token_Kind.DEC] 
  assert token_value_list == ["12.3", ".987"] 
  
# ---
