import sys

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

ASSIGNMENT_OPERATORS = [
  TR_Node_Kind.ASSIGN,
  TR_Node_Kind.ASSIGN_ADD,
  TR_Node_Kind.ASSIGN_SUB,
  TR_Node_Kind.ASSIGN_MUL,
  TR_Node_Kind.ASSIGN_DIV,
  TR_Node_Kind.ASSIGN_MOD,
  TR_Node_Kind.ASSIGN_POW
]

BOOL_VALUE_TABLE = {
  "true": True,
  "false": False,
}

# ---

class Evaluator:
  def __init__(self):
    self.env = {}

  def eval(self, node):
    node_kind = node.kind

    if node_kind == TR_Node_Kind.INT:
      ret = self.eval_int(node)

    elif node_kind == TR_Node_Kind.DEC:
      ret = self.eval_dec(node)

    elif node_kind == TR_Node_Kind.STR:
      ret = self.eval_str(node)

    elif node_kind == TR_Node_Kind.BOOL:
      ret = self.eval_bool(node)

    elif node_kind == TR_Node_Kind.VAR:
      ret = self.eval_var(node)

    elif node_kind == TR_Node_Kind.MINUS:
      ret = self.eval_unary(node)

    elif node_kind in ARITHMETIC_OPERATORS:
      ret = self.eval_arithemetic_operation(node)

    elif node_kind in ASSIGNMENT_OPERATORS:
      ret = self.eval_assignment_operation(node)

    else:
      print("ERROR:", node_kind)
      sys.exit()

    return ret

  # ---
  # 各ノードの評価
  def eval_int(self, node):
    value = node.value
    return int(value)

  def eval_dec(self, node):
    value = node.value
    return float(value)

  def eval_str(self, node):
    value = node.value
    return value

  def eval_bool(self, node):
    value = BOOL_VALUE_TABLE[node.value]
    return value

  def eval_var(self, node):
    name = node.value
    if name in self.env:
      return self.env[name]
    else:
      print("ERROR:", name)
      sys.exit()

  def eval_unary(self, node):
    if node.kind == TR_Node_Kind.MINUS:
      return -self.eval(node.right)

  def eval_arithemetic_operation(self, node):
    left = self.eval(node.left)
    right = self.eval(node.right)
    oper = node.kind

    if oper == TR_Node_Kind.ADD: ret = left + right
    elif oper == TR_Node_Kind.SUB: ret = left - right
    elif oper == TR_Node_Kind.MUL: ret = left * right
    elif oper == TR_Node_Kind.DIV: ret = left / right
    elif oper == TR_Node_Kind.MOD: ret = left % right
    elif oper == TR_Node_Kind.POW: ret = left ** right

    return ret

  def eval_assignment_operation(self, node):
    var = node.var
    expr = node.expr
    value = self.eval(node.expr)
    self.assign(var, value)

    return value

  # ---
  
  def assign(self, var, value):
    name = var.value
    self.env[name] = value

# ---

def tori_minus_run(trees):
  evaluator = Evaluator()
  for tree in trees:
    value = evaluator.eval(tree)
    print(value)

# ---
