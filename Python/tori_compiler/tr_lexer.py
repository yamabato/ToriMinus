import string

from tr_token import TR_Token, TR_Token_Kind

NUMBER = string.digits
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

  elif char in NUMBER: return "NUMBER"

# ---
# 各種リテラル読み込み

def read_digits(program, n):
  token_value = ""
  c = get_current_char(program, n)

  while check_char_type(c) == "NUMBER": 
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

# ---

def tr_lexer(program):
  program_length = len(program)

  tokens = []
  n = 0
  
  while n < program_length:
    c = get_current_char(program, n)

    # Token_Kind.INT, Token_Kind.DEC
    if c in NUMBER or c == ".":
      kind, value, n = read_numerical_literal(program, n)
      token = TR_Token(kind, value)
      tokens.append(token)

    n, c = get_next_char(program, n)

  return tokens 

# ---
