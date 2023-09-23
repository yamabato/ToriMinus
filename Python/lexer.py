import string

from token import Token, Token_Kind

NUMBER = string.digits
WHITESPACE = " \t\n"

def next_char(program, n):
  if len(program) <= n+1: return n+1, ""
  
  n += 1
  return n, program[n]

def lexer(program):
  program_length = len(program)

  tokens = []
  n = 0
  
  while n < program_length:
    token_value = ""
    c = program[n]

    # Token_Kind.INT
    if c in NUMBER:
      while c in NUMBER:
        token_value += c
        n, c = next_char(program, n)
      token = Token(Token_Kind.INT, token_value)
      tokens.append(token)

    n, c = next_char(program, n)

  return tokens 
