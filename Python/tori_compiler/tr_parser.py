import sys

from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node, TR_Node_Kind


ASSIGNMENT_OPERS = [
  "=", "+=", "-=", "*=", "/=", "%=", "**=",
]

ASSIGN_OPER_KIND = {
  "=": TR_Node_Kind.ASSIGN,
  "+=": TR_Node_Kind.ASSIGN_ADD,
  "-=": TR_Node_Kind.ASSIGN_SUB,
  "*=": TR_Node_Kind.ASSIGN_MUL,
  "/=": TR_Node_Kind.ASSIGN_DIV,
  "%=": TR_Node_Kind.ASSIGN_MOD,
  "**=": TR_Node_Kind.ASSIGN_POW,
}

COMPARISON_OPERS = [
  "==", "!=", "<", ">", "<=", ">=",
]

COMPARISON_OPER_KIND = {
  "==": TR_Node_Kind.EQUAL,
  "!=": TR_Node_Kind.NEQ,
  "<": TR_Node_Kind.LT,
  ">": TR_Node_Kind.GT,
  "<=": TR_Node_Kind.LEQ,
  ">=": TR_Node_Kind.GEQ,
}

# ---
# ヘルパー関数

def get_current_token(tokens, n):
  if n < 0 or len(tokens) <= n: return TR_Token()
  return tokens[n]

def get_next_token(tokens, n):
  n += 1
  return get_current_token(tokens, n), n

def peek_next_token(tokens, n):
  return get_current_token(tokens, n+1)

def get_prev_token(tokens, n):
  return get_current_token(tokens, n-1)

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
  node, n = parse_assignment(tokens, n) 

  return node, n

def parse_assignment(tokens, n):
  token = get_current_token(tokens, n)
  next_token = peek_next_token(tokens, n)

  if token.kind == TR_Token_Kind.IDENT and \
      next_token.kind == TR_Token_Kind.PUNCT and next_token.value in ASSIGNMENT_OPERS:
    var, n = parse_var(tokens, n)
    expr, n = parse_expression(tokens, n+1)

    node = TR_Node()
    node.kind = ASSIGN_OPER_KIND[next_token.value]
    node.var = var 
    node.expr = expr 

  else:
    node, n = parse_comparison(tokens, n)
  
  return node, n

def parse_comparison(tokens, n):
  node, n = parse_add_sub(tokens, n)

  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value in COMPARISON_OPERS:
    right, n = parse_add_sub(tokens, n+1)
    
    node = make_binary_operation_node(COMPARISON_OPER_KIND[token.value], node, right)

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
  node, n = parse_func_call(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "**":
      right, n = parse_factor(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.POWER, node, right)
    else: break

  return node, n

def parse_func_call(tokens, n):
  node, n = parse_pyfunc_call(tokens, n)

  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value == "(":
    args = []
    args, n = parse_arg_list(tokens, n+1) 

    n += 1
    func = node
    node = TR_Node()
    node.kind = TR_Node_Kind.CALL
    node.func = func 
    node.args = args
   
  return node, n

def parse_pyfunc_call(tokens, n):
  token = get_current_token(tokens, n)

  if token.kind == TR_Token_Kind.PYFUNC_IDENT:
    next_token, n = get_next_token(tokens, n)

    if next_token.kind == TR_Token_Kind.PUNCT and next_token.value == "(":
      name = token.value

      args = []
      args, n = parse_arg_list(tokens, n+1) 

      n += 1
      node = TR_Node()
      node.kind = TR_Node_Kind.PYFUNC_CALL
      node.name = name 
      node.args = args
 
    else:
      print("ERROR")
      sys.exit()

  else:  
    node, n = parse_factor(tokens, n)

  return node, n

def parse_factor(tokens, n):
  token = get_current_token(tokens, n)
  next_token = peek_next_token(tokens, n)

  if token.kind == TR_Token_Kind.INT:
    node, n = parse_int(tokens, n)

  elif token.kind == TR_Token_Kind.DEC:
    node, n = parse_dec(tokens, n)

  elif token.kind == TR_Token_Kind.STRING:
    node, n = parse_str(tokens, n)

  elif token.kind == TR_Token_Kind.IDENT:
    node, n = parse_var(tokens, n)

  elif token.kind == TR_Token_Kind.PUNCT and token.value == "(":
    node, n = parse_expression(tokens, n+1)
    n += 1

  elif token.kind == TR_Token_Kind.IDENT:
    node, n = parse_var(tokens, n)

  elif token.kind == TR_Token_Kind.PUNCT and token.value == "{" and \
        next_token.kind == TR_Token_Kind.PUNCT and next_token.value == "(": # 関数定義
    node, n = parse_define_function(tokens, n)

  return node, n

def parse_int(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.INT
  token = get_current_token(tokens, n)
  node.value = int(token.value)

  return node, n+1

def parse_dec(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.DEC
  token = get_current_token(tokens, n)
  node.value = float(token.value)

  return node, n+1

def parse_str(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.STR
  token = get_current_token(tokens, n)
  node.value = token.value

  return node, n+1

def parse_var(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.VAR
  token = get_current_token(tokens, n)
  node.value = token.value

  return node, n+1

def parse_arg_list(tokens, n):
  args = []

  while n < len(tokens):
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ")": break

    else:
      arg, n = parse_expression(tokens, n)
      args.append(arg)

    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ",":
      n += 1
    elif token.kind == TR_Token_Kind.PUNCT and token.value == ")": break
    else:
      print("ERROR")
      sys.exit()

  return args, n

def parse_def_expressions(tokens, n):
  exprs = []

  while n < len(tokens):
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
 
    expr, n = parse_expression(tokens, n)
    exprs.append(expr)

    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ",": n += 1 
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    else:
      print("ERROR")
      sys.exit()

  return exprs, n+1

def parse_define_function(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.DEF
  node.args = []
  node.exprs = []

  n += 2
  args, n = parse_arg_list(tokens, n)
  node.args = args

  n += 1
  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value == "}":
    n += 1
  elif token.kind == TR_Token_Kind.PUNCT and token.value == ",":
    exprs, n = parse_def_expressions(tokens, n+1)
    node.exprs = exprs
  else:
    print("ERROR")
    sys.exit()
  
  return node, n

# ---

def tr_parser(tokens):
  tokens_count = len(tokens)

  tree = None
  trees = []
  n = 0

  while n < tokens_count:
    token = get_current_token(tokens, n)
    next_token = peek_next_token(tokens, n)

    if token.kind == TR_Token_Kind.INT or token.kind == TR_Token_Kind.DEC: # 数値
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.STRING: # 文字列
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.IDENT: # 変数
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.PYFUNC_IDENT: # pyfunc 
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.PUNCT and (token.value == "+" or token.value == "-"): # 単項演算子
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "{" and \
          next_token.kind == TR_Token_Kind.PUNCT and next_token.value == "(": # 関数定義
      tree, n = parse_expression(tokens, n)
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "(": # 括弧
      tree, n = parse_expression(tokens, n)
    else:
      print("ERROR", token.value, token.kind, next_token.value, next_token.kind)
      sys.exit()
    
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ";":
      n += 1
    else:
      print("ERROR")
      sys.exit()

    trees.append(tree)
      
  return trees
   
# ---
