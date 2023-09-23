import string

from tr_token import TR_Token, TR_Token_Kind

NUMBER = string.digits
WHITESPACE = " \t\n"

# ---
# ヘルパー関数

def next_char(program, n):
  if len(program) <= n+1: return n+1, ""
  
  n += 1
  return n, program[n]

def check_char_type(char):
  if char == "": return None

  elif char in NUMBER: return "NUMBER"

# ---
# 各種リテラル読み込み

def read_numerical_literal(program, n):
  token_value = ""
  c = program[n]
  while check_char_type(c) == "NUMBER": 
    token_value += c
    n, c = next_char(program, n)
  
  kind = TR_Token_Kind.INT
  return kind, token_value, n

# ---

def tr_lexer(program):
  program_length = len(program)

  tokens = []
  n = 0
  
  while n < program_length:
    c = program[n]

    # Token_Kind.INT, Token_Kind.DEC
    if c in NUMBER or c == ".":
      kind, value, n = read_numerical_literal(program, n)
      token = TR_Token(kind, value)
      tokens.append(token)

    n, c = next_char(program, n)

  return tokens 
