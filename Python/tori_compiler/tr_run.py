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

    elif node_kind in ARITHMETIC_OPERATORS:
      ret = eval_arithemetic_operation(node)

    return ret

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

# ---

def tori_minus_run(trees):
  evaluator = Evaluator()
  for tree in trees:
    value = evaluator.eval(tree)
    print(value)

# ---
