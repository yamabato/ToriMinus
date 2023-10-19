import sys

from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node, TR_Node_Kind


ASSIGNMENT_OPERS = [
  "=", "+=", "-=", "*=", "/=", "%=", "**=", "&=", "|=", "^="
]

ASSIGN_OPER_KIND = {
  "=": TR_Node_Kind.ASSIGN,
  "+=": TR_Node_Kind.ASSIGN_ADD,
  "-=": TR_Node_Kind.ASSIGN_SUB,
  "*=": TR_Node_Kind.ASSIGN_MUL,
  "/=": TR_Node_Kind.ASSIGN_DIV,
  "%=": TR_Node_Kind.ASSIGN_MOD,
  "**=": TR_Node_Kind.ASSIGN_POW,
  "&=": TR_Node_Kind.ASSIGN_AND,
  "|=": TR_Node_Kind.ASSIGN_OR,
  "^=": TR_Node_Kind.ASSIGN_XOR,
}

CALC_ASSIGN_OPER_TABLE = {
  "+=": TR_Node_Kind.ADD,
  "-=": TR_Node_Kind.SUB,
  "*=": TR_Node_Kind.MUL,
  "/=": TR_Node_Kind.DIV,
  "%=": TR_Node_Kind.MOD,
  "**=": TR_Node_Kind.POW,
  "&=": TR_Node_Kind.AND,
  "|=": TR_Node_Kind.OR,
  "^=": TR_Node_Kind.XOR,
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

def make_binary_operation_node(kind, left, right):
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

def check_token(token, kind, value):
  if token.kind != kind or token.value != value:
    print("ERROR")
    sys.exit()

# ---
# 各種構文の解析

def parse_if(tokens, n):
  token, n = get_next_token(tokens, n)

  node = TR_Node()
  node.kind = TR_Node_Kind.IF

  cond, n = parse_expression(tokens, n)
  node.cond = cond 

  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, "{")
  token, n = get_next_token(tokens, n)
  
  if_stmts = [] 
  else_stmts = [] 
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    stmt, n = parse_statement(tokens, n)
    if_stmts.append(stmt)
  n += 1
  node.if_stmts = if_stmts

  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.IDENT and token.value == "else":
    n += 1
  else:
    return node, n

  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.IDENT and token.value == "if":
    else_stmt, n = parse_if(tokens, n)
    node.else_stmts = [else_stmt]
    return node, n
  check_token(token, TR_Token_Kind.PUNCT, "{")

  token, n = get_next_token(tokens, n)
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    stmt, n = parse_statement(tokens, n)
    else_stmts.append(stmt)
  node.else_stmts = else_stmts

  return node, n+1
 
def parse_while(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.WHILE

  token, n = get_next_token(tokens, n)

  cond, n = parse_expression(tokens, n)
  node.cond = cond

  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, "{")

  token, n = get_next_token(tokens, n)
  stmts = []
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    stmt, n = parse_statement(tokens, n)
    stmts.append(stmt)

  node.stmts = stmts
  return node, n+1

def parse_for(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.FOR

  token, n = get_next_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, "(")

  init, n = parse_expression(tokens, n+1)
  node.init = init
  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, ",")
  n += 1

  cond, n = parse_expression(tokens, n)
  node.cond = cond 
  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, ",")
  n += 1

  adv, n = parse_expression(tokens, n)
  node.adv = adv

  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, ")")
  n += 1
  token = get_current_token(tokens, n)
  check_token(token, TR_Token_Kind.PUNCT, "{")
  n += 1

  stmts = []
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    stmt, n = parse_statement(tokens, n)
    stmts.append(stmt)

  node.stmts = stmts
  return node, n+1

def parse_expression(tokens, n):
  node, n = parse_assignment(tokens, n) 

  return node, n

def parse_assignment(tokens, n):
  token = get_current_token(tokens, n)
  next_token = peek_next_token(tokens, n)

  if token.kind == TR_Token_Kind.IDENT and \
      next_token.kind == TR_Token_Kind.PUNCT and next_token.value in ASSIGNMENT_OPERS:
    var, n = parse_var(tokens, n)
    oper_token = next_token.value
    expr, n = parse_expression(tokens, n+1)

    if oper_token in CALC_ASSIGN_OPER_TABLE:
      oper = CALC_ASSIGN_OPER_TABLE[oper_token]
      expr = make_binary_operation_node(oper, var, expr)

    node = TR_Node()
    node.kind = TR_Node_Kind.ASSIGN
    node.var = var
    node.expr = expr 

  else:
    node, n = parse_comparison(tokens, n)
  
  return node, n

def parse_comparison(tokens, n):
  node, n = parse_or(tokens, n)

  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value in COMPARISON_OPERS:
    right, n = parse_or(tokens, n+1)
    
    node = make_binary_operation_node(COMPARISON_OPER_KIND[token.value], node, right)

  return node, n

def parse_or(tokens, n):
  node, n = parse_xor(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "|":
      right, n = parse_xor(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.OR, node, right)
    else: break

  return node, n

def parse_xor(tokens, n):
  node, n = parse_and(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "^":
      right, n = parse_and(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.XOR, node, right)
    else: break

  return node, n

def parse_and(tokens, n):
  node, n = parse_add_sub(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "&":
      right, n = parse_add_sub(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.AND, node, right)
    else: break

  return node, n

def parse_add_sub(tokens, n):
  node, n = parse_mul_div(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "+":
      right, n = parse_mul_div(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.ADD, node, right)
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "-":
      right, n = parse_mul_div(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.SUB, node, right)
    else: break

  return node, n

def parse_mul_div(tokens, n):
  node, n = parse_unary(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "*":
      right, n = parse_unary(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.MUL, node, right)
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "/":
      right, n = parse_unary(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.DIV, node, right)
    elif token.kind == TR_Token_Kind.PUNCT and token.value == "%":
      right, n = parse_unary(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.MOD, node, right)
    else: break

  return node, n

def parse_unary(tokens, n):
  token = get_current_token(tokens, n) 

  if token.kind == TR_Token_Kind.PUNCT and token.value == "+":
    node, n = parse_power(tokens, n+1)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "-":
    right, n = parse_power(tokens, n+1)
    node = make_unary_node(TR_Node_Kind.MINUS, right)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "!":
    right, n = parse_power(tokens, n+1)
    node = make_unary_node(TR_Node_Kind.NOT, right)
  else:
    node, n = parse_power(tokens, n)

  return node, n

def parse_power(tokens, n):
  node, n = parse_func_call(tokens, n)

  while True:
    token = get_current_token(tokens, n) 
    if token.kind == TR_Token_Kind.PUNCT and token.value == "**":
      right, n = parse_factor(tokens, n+1)
      node = make_binary_operation_node(TR_Node_Kind.POW, node, right)
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
      print("ERROR-PARSER")
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

  elif token.kind == TR_Token_Kind.PUNCT and token.value == "[":
    node, n = parse_list(tokens, n)

  elif token.kind == TR_Token_Kind.BOOL:
    node, n = parse_bool(tokens, n)

  elif token.kind == TR_Token_Kind.NON:
    node, n = parse_non(tokens, n)

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

def parse_list(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.LIST
  
  elems = []
  n += 1
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "]": break
    elem, n = parse_expression(tokens, n)
    elems.append(elem)
    
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ",": n += 1

  node.elems = elems
  return node, n+1

def parse_bool(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.BOOL
  token = get_current_token(tokens, n)
  node.value = token.value

  return node, n+1

def parse_non(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.NON
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
      print("ERROR-PARSER")
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
      print("ERROR-PARSER")
      sys.exit()

  return exprs, n+1

def parse_def_statements(tokens, n):
  stmts = []

  while n < len(tokens):
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
 
    stmt, n = parse_statement(tokens, n)
    stmts.append(stmt)

    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == "}": break
    """
    else:
      print("ERROR-PARSER-def-stmts")
      sys.exit()
    """

  return stmts, n+1

def parse_define_function(tokens, n):
  node = TR_Node()
  node.kind = TR_Node_Kind.DEF
  node.args = []
  node.exprs = []
  node.stmts = []

  n += 2
  args, n = parse_arg_list(tokens, n)
  node.args = args

  n += 1
  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value == "}":
    n += 1
  elif token.kind == TR_Token_Kind.PUNCT and token.value == ",":
    #exprs, n = parse_def_expressions(tokens, n+1)
    stmts, n = parse_def_statements(tokens, n+1)
    #node.exprs = exprs
    node.stmts = stmts 
  else:
    print("ERROR-PARSER")
    sys.exit()
  
  return node, n

def parse_return(tokens, n):
	node = TR_Node()
	node.kind = TR_Node_Kind.RETURN

	token, n = get_next_token(tokens, n)
	if token.kind == TR_Token_Kind.PUNCT and token.value == ";":
		return node, n

	expr, n = parse_expression(tokens, n)
	node.expr = expr

	token = get_current_token(tokens, n)
	if token.kind != TR_Token_Kind.PUNCT or token.value != ";":
		print("ERROR-RETURN")
		sys.exit()

	return node, n


def parse_pyfunc(tokens, n):
  n += 1
  
  funcs = []
  while True:
    token = get_current_token(tokens, n)
    if token.kind == TR_Token_Kind.PYFUNC_IDENT:
      funcs.append(token.value)
    else:
      print("ERROR-PARSER")
      sys.exit()

    token, n = get_next_token(tokens, n)
    if token.kind == TR_Token_Kind.PUNCT and token.value == ",": n += 1
    elif token.kind == TR_Token_Kind.PUNCT and token.value == ";": break
    else:
      print("ERROR-PARSER")
      sys.exit()

  node = TR_Node()
  node.kind = TR_Node_Kind.PYFUNC
  node.funcs = funcs

  return node, n

# ---

def parse_statement(tokens, n):
  token = get_current_token(tokens, n)
  next_token = peek_next_token(tokens, n)

  if token.kind == TR_Token_Kind.INT or token.kind == TR_Token_Kind.DEC: # 数値
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.STRING: # 文字列
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "[": # リスト 
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.BOOL: # 真偽値 
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.NON: # non 
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.PYFUNC_IDENT: # pyfunc 
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.PUNCT and (token.value == "+" or token.value == "-" or token.value == "!"): # 単項演算子
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "{" and \
        next_token.kind == TR_Token_Kind.PUNCT and next_token.value == "(": # 関数定義
    tree, n = parse_expression(tokens, n)
  elif token.kind == TR_Token_Kind.PUNCT and token.value == "(": # 括弧
    tree, n = parse_expression(tokens, n)

  elif token.kind == TR_Token_Kind.IDENT:
    if token.value == "if": # if
      tree, n = parse_if(tokens, n)
    elif token.value == "while": # while
      tree, n = parse_while(tokens, n)
    elif token.value == "for": # for
      tree, n = parse_for(tokens, n)
    elif token.value == "return": # return
      tree, n = parse_return(tokens, n)
    else: # 変数
      tree, n = parse_expression(tokens, n)

  else:
    print("ERROR-PARSER", token.value, token.kind, next_token.value, next_token.kind)
    sys.exit()
  
  token = get_current_token(tokens, n)
  if token.kind == TR_Token_Kind.PUNCT and token.value == ";":
    n += 1
  else:
    print("ERROR-PARSER")
    sys.exit()

  return tree, n


def tr_parser(tokens):
  tokens_count = len(tokens)

  tree = None
  trees = []
  n = 0

  while n < tokens_count:
    tree, n = parse_statement(tokens, n)
    trees.append(tree)
      
  return trees
   
# ---
