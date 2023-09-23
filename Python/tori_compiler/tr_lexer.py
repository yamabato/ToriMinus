import string

from tr_token import TR_Token, TR_Token_Kind

NUMBER = string.digits
WHITESPACE = " \t\n"

def next_char(program, n):
  if len(program) <= n+1: return n+1, ""
  
  n += 1
  return n, program[n]

def check_char_type(char):
  if char == "": return None

  elif char in NUMBER: return "NUMBER"

def tr_lexer(program):
  program_length = len(program)

  tokens = []
  n = 0
  
  while n < program_length:
    token_value = ""
    c = program[n]

    # Token_Kind.INT
    if c in NUMBER:
      while check_char_type(c) == "NUMBER": 
        token_value += c
        n, c = next_char(program, n)
      token = TR_Token(TR_Token_Kind.INT, token_value)
      tokens.append(token)

    n, c = next_char(program, n)

  return tokens 
