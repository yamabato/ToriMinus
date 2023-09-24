from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node, TR_Node_Kind

# ---
# ヘルパー関数

def get_current_token(tokens, n):
  if len(tokens) <= n: return TR_Token()
  return tokens[n]

def get_next_token(tokens, n):
  n += 1
  return n, get_current_token(tokens, n)

# ---

def parse_expression(tokens, n):
  node, n = parse_comparison(tokens, n) 

  return node, n

def parse_comparison(tokens, n):
  node, n = parse_add_sub(tokens, n)

  return node, n

def parse_add_sub(tokens, n):
  node, n = parse_mul_div(tokens, n)

  return node, n

def parse_mul_div(tokens, n):
  node, n = parse_unary(tokens, n)

  return node, n

def parse_unary(tokens, n):
  node, n = parse_power(tokens, n)

  return node, n

def parse_power(tokens, n):
  node, n = parse_factor(tokens, n)

  return node, n

def parse_factor(tokens, n):
  node, n = parse_int(tokens, n)

  return node, n

def parse_int(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.INT
  token = get_current_token(tokens, n)
  node.value = int(token.value)

  return node, n+1

# ---

def tr_parser(tokens):
  tokens_count = len(tokens)

  trees = []
  n = 0

  while n < tokens_count:
    token = get_current_token(tokens, n)
    token_kind = token.kind

    if token_kind == TR_Token_Kind.INT or token_kind == TR_Token_Kind.DEC:
      tree, n = parse_expression(tokens, n)

    trees.append(tree)
      
  return trees
   
# ---
