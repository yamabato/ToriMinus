import sys

from tr_node import TR_Node_Kind
from tr_value import TR_Value, TR_Value_Kind

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

COMPARISON_OPERATORS = [
  TR_Node_Kind.EQUAL,
  TR_Node_Kind.NEQ,
  TR_Node_Kind.LT,
  TR_Node_Kind.GT,
  TR_Node_Kind.LEQ,
  TR_Node_Kind.GEQ,
]

BOOL_VALUE_TABLE = {
  "true": True,
  "false": False,
}

# ---

def bool_to_tr_bool(value):
  if value: return "true"
  return "false"

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

    elif node_kind == TR_Node_Kind.NON:
      ret = self.eval_non(node)

    elif node_kind == TR_Node_Kind.VAR:
      ret = self.eval_var(node)

    elif node_kind == TR_Node_Kind.MINUS:
      ret = self.eval_unary(node)

    elif node_kind in ARITHMETIC_OPERATORS:
      ret = self.eval_arithemetic_operation(node)

    elif node_kind in ASSIGNMENT_OPERATORS:
      ret = self.eval_assignment_operation(node)

    elif node_kind in COMPARISON_OPERATORS:
      ret = self.eval_comparison_operation(node)

    else:
      print("ERROR:", node_kind)
      sys.exit()

    return ret

  # ---
  # 各ノードの評価
  def eval_int(self, node):
    tr_value = TR_Value()
    tr_value.kind = TR_Value_Kind.num_
    tr_value.value = node.value
    return tr_value

  def eval_dec(self, node):
    tr_value = TR_Value()
    tr_value.kind = TR_Value_Kind.num_
    tr_value.value = node.value
    return tr_value

  def eval_str(self, node):
    tr_value = TR_Value()
    tr_value.kind = TR_Value_Kind.str_
    tr_value.value = node.value
    return tr_value

  def eval_bool(self, node):
    tr_value = TR_Value()
    tr_value.kind = TR_Value_Kind.bool_
    tr_value.value = node.value
    return tr_value

  def eval_non(self, node):
    tr_value = TR_Value()
    tr_value.kind = TR_Value_Kind.non_
    return tr_value

  def eval_var(self, node):
    name = node.value
    if name in self.env:
      return self.env[name]
    else:
      print("ERROR:", name)
      sys.exit()

  def eval_unary(self, node):
    if node.kind == TR_Node_Kind.MINUS:
      ret = TR_Value()
      value = self.eval(node.right)
      if value.kind == TR_Value_Kind.num_:
        ret.kind = TR_Value_Kind.num_
        ret.value = -value.value
      else:
        print("ERROR")
        sys.exit

    return ret

  def eval_arithemetic_operation(self, node):
    left = self.eval(node.left)
    right = self.eval(node.right)

    left_kind = left.kind
    right_kind = right.kind

    left_value = left.value
    right_value = right.value

    oper = node.kind
    
    if left_kind == TR_Value_Kind.num_ and right_kind == TR_Value_Kind.num_:
      if oper == TR_Node_Kind.ADD: ret_value = left_value + right_value
      elif oper == TR_Node_Kind.SUB: ret_value = left_value - right_value
      elif oper == TR_Node_Kind.MUL: ret_value = left_value * right_value
      elif oper == TR_Node_Kind.DIV: ret_value = left_value / right_value
      elif oper == TR_Node_Kind.MOD: ret_value = left_value % right_value
      elif oper == TR_Node_Kind.POW: ret_value = left_value ** right_value
      else:
        print("ERROR")
        sys.exit()

      ret = TR_Value()
      ret.kind = TR_Value_Kind.num_
      ret.value = ret_value

    elif left_kind == TR_Value_Kind.str_ and right_kind == TR_Value_Kind.num_:
      if oper == TR_Node_Kind.MUL: ret_value = left_value * int(right_value)
      else:
        print("ERROR")
        sys.exit()

      ret = TR_Value()
      ret.kind = TR_Value_Kind.str_
      ret.value = ret_value

    elif left_kind == TR_Value_Kind.str_ and right_kind == TR_Value_Kind.str_:
      if oper == TR_Node_Kind.ADD: ret_value = left_value + right_value
      else:
        print("ERROR")
        sys.exit()

      ret = TR_Value()
      ret.kind = TR_Value_Kind.str_
      ret.value = ret_value

    else:
      print("ERROR")
      sys.exit()

    return ret

  def eval_assignment_operation(self, node):
    var = node.var
    expr = node.expr
    value = self.eval(node.expr)
    self.assign(var, value)

    return value

  def eval_comparison_operation(self, node):
    left = self.eval(node.left)
    right = self.eval(node.right)

    left_kind = left.kind
    right_kind = right.kind

    left_value = left.value
    right_value = right.value

    oper = node.kind
    
    if oper == TR_Node_Kind.EQUAL:
      ret_value = (left_kind == right_kind) & (left_value == right_value)
    elif oper == TR_Node_Kind.NEQ:
      ret_value = (left_kind != right_kind) | (left_value != right_value)
    elif oper == TR_Node_Kind.LT:
      if left_kind == TR_Value_Kind.num_ and right_kind == TR_Value_Kind.num_:
        ret_value = left_value < right_value
      else:
        print("ERROR")
        sys.exit()
    elif oper == TR_Node_Kind.GT:
      if left_kind == TR_Value_Kind.num_ and right_kind == TR_Value_Kind.num_:
        ret_value = left_value > right_value
      else:
        print("ERROR")
        sys.exit()
    elif oper == TR_Node_Kind.LEQ:
      if left_kind == TR_Value_Kind.num_ and right_kind == TR_Value_Kind.num_:
        ret_value = left_value <= right_value
      else:
        print("ERROR")
        sys.exit()
    elif oper == TR_Node_Kind.GEQ:
      if left_kind == TR_Value_Kind.num_ and right_kind == TR_Value_Kind.num_:
        ret_value = left_value >= right_value
      else:
        print("ERROR")
        sys.exit()

    ret = TR_Value()
    ret.kind = TR_Value_Kind.bool_
    ret.value = bool_to_tr_bool(ret_value)
    return ret

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
