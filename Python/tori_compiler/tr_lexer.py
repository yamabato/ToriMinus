import string

from tr_token import TR_Token, TR_Token_Kind, TR_Char_Type

DIGITS = string.digits
LATIN_ALPHABET = string.ascii_letters
WHITESPACE = " \t\n"

# ---
# ヘルパー関数

def get_current_char(program, n):
  if len(program) <= n: return ""
  return program[n]

def get_next_char(program, n):
  n += 1
  return n, get_current_char(program, n) 

def check_char_type(char):
  if char == "": return None
  
  elif char in WHITESPACE: return TR_Char_Type.WHITESPACE 
  elif char in DIGITS: return TR_Char_Type.DIGIT 
  elif char in LATIN_ALPHABET or char == "_": return TR_Char_Type.IDENT 

# ---
# 各種リテラル読み込み

def read_digits(program, n):
  token_value = ""
  c = get_current_char(program, n)

  while check_char_type(c) == TR_Char_Type.DIGIT: 
    token_value += c
    n, c = get_next_char(program, n)

  kind = TR_Token_Kind.INT
  return kind, token_value, n

def read_numerical_literal(program, n):
  token_value = ""
  kind = TR_Token_Kind.INT

  _, digits, n = read_digits(program, n)
  token_value = digits

  c = get_current_char(program, n)
  if c == ".":
    kind = TR_Token_Kind.DEC
    token_value += "."
    n, c = get_next_char(program, n)

  _, digits, n = read_digits(program, n)
  token_value += digits
  
  return kind, token_value, n

def read_ident_literal(program, n):
  kind = TR_Token_Kind.IDENT
  token_value = ""

  c = get_current_char(program, n)

  while check_char_type(c) in [TR_Char_Type.IDENT, TR_Char_Type.DIGIT]: 
    token_value += c
    n, c = get_next_char(program, n)

  return kind, token_value, n

# ---

def tr_lexer(program):
  program_length = len(program)

  tokens = []
  n = 0
  
  while n < program_length:
    c = get_current_char(program, n)

    char_type = check_char_type(c)
   
    # 読み飛ばし 
    if char_type == TR_Char_Type.WHITESPACE: 
      n, c = get_next_char(program, n)

    # Token_Kind.INT, Token_Kind.DEC
    elif char_type == TR_Char_Type.DIGIT or c == ".":
      kind, value, n = read_numerical_literal(program, n)
      token = TR_Token(kind, value)
      tokens.append(token)

    # Token_Kind.IDENT
    elif char_type == TR_Char_Type.IDENT: 
      kind, value, n = read_ident_literal(program, n)
      print(value)
      token = TR_Token(kind, value)
      tokens.append(token)

  return tokens 

# ---
