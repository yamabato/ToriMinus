from tori_test import *
from lexer_test_util import *

#---
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
