from tr_token import TR_Token, TR_Token_Kind

# ---
# ヘルパー関数

def get_current_token(tokens, n):
  if len(tokens) >= n: return TR_Token 
  return tokens[n]

def get_next_token(tokens, n):
  n += 1
  return n, get_current_token(tokens, n)

# ---

# ---

def tr_parser(tokens):
  tokens_count = len(tokens)

  tree = []
  n = 0

  while n < tokens_count:
    pass

  return tree
   
# ---
