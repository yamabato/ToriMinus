from tr_node import TR_Node_Kind

# ---
# 定数等の設定

ARITHMETIC_OPERATORS = [
  TR_Node_Kind.ADD,
  TR_Node_Kind.SUB,
  TR_Node_Kind.MUL,
  TR_Node_Kind.DIV,
  TR_Node_Kind.MOD,
  TR_Node_Kind.POW
]

# ---
# 各nodeの処理
def eval_arithemetic_operation(node):
  left = tr_eval(node.left)
  right = tr_eval(node.right)
  oper = node.kind

  if oper == TR_Node_Kind.ADD: ret = left + right
  elif oper == TR_Node_Kind.SUB: ret = left - right
  elif oper == TR_Node_Kind.MUL: ret = left * right
  elif oper == TR_Node_Kind.DIV: ret = left / right
  elif oper == TR_Node_Kind.MOD: ret = left % right
  elif oper == TR_Node_Kind.POW: ret = left ** right

  return ret

def eval_int(node):
  value = node.value
  return int(value)

# ---

def tr_eval(node):
  node_kind = node.kind

  if node_kind in ARITHMETIC_OPERATORS:
    ret = eval_arithemetic_operation(node)

  elif node_kind == TR_Node_Kind.INT:
    ret = eval_int(node)

  return ret

def tori_minus_run(trees):
  for tree in trees:
    value = tr_eval(tree)
    print(value)

# ---
