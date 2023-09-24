import sys

from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node, TR_Node_Kind

# ---
# ヘルパー関数

def get_current_token(tokens, n):
  if len(tokens) <= n: return TR_Token()
  return tokens[n]

def get_next_token(tokens, n):
  n += 1
  return get_current_token(tokens, n), n

def peek_next_token(tokens, n):
  return get_current_token(tokens, n+1)

def make_binary_operation_node(kind,left, right):
  node = TR_Node()
  node.kind = kind
  node.right = right
  node.left = left

  return node

def make_unary_node(kind, right):
  node = TR_Node()
  node.kind = kind
  node.right = right
   
  return node

# ---
# 各種構文の解析

def parse_expression(tokens, n):
  node, n = parse_comparison(tokens, n) 

  return node, n

def parse_comparison(tokens, n):
  node, n = parse_add_sub(tokens, n)

  return node, n

def parse_add_sub(tokens, n):
  node, n = parse_mul_div(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "+":
      right, n = parse_mul_div(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.ADD, node, right)
    else: break

  return node, n

def parse_mul_div(tokens, n):
  node, n = parse_unary(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "*":
      right, n = parse_unary(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.MUL, node, right)
    else: break

  return node, n

def parse_unary(tokens, n):
  token = get_current_token(tokens, n) 

  if token.kind == TR_Token_Kind.PUNCT and token.value == "+":
    node, n = parse_power(tokens, n+1)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "-":
    right, n = parse_power(tokens, n+1)
    node = make_unary_node(TR_Node_Kind.MINUS, right)
  else:
    node, n = parse_power(tokens, n)

  return node, n

def parse_power(tokens, n):
  node, n = parse_factor(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "**":
      right, n = parse_factor(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.POWER, node, right)
    else: break

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

  tree = None
  trees = []
  n = 0

  while n < tokens_count:
    token = get_current_token(tokens, n)
    token_kind = token.kind
    token_value = token.value

    if token_kind == TR_Token_Kind.INT or token_kind == TR_Token_Kind.DEC:
      tree, n = parse_expression(tokens, n)
    elif token_kind == TR_Token_Kind.PUNCT and (token_value == "+" or token_value == "-"): 
      tree, n = parse_expression(tokens, n)

    trees.append(tree)
      
  return trees
   
# ---
