from tori_test import *

# ---
# ヘルパー関数類

def expand_trees(trees):
  expanded_code = ""

  for tree in trees:
    expanded_code += expand_tree(tree)

  return expanded_code

def expand_tree(tree):
  expanded = ""

  node_type = tree.kind

  if node_type == TR_Node_Kind.INT:
    expanded += f"INT({tree.value})"

  elif node_type == TR_Node_Kind.DEC:
    expanded += f"DEC({tree.value})"

  elif node_type == TR_Node_Kind.STR:
    expanded += f"STR({tree.value})"

  elif node_type == TR_Node_Kind.VAR:
    expanded += f"VAR({tree.value})"

  elif node_type == TR_Node_Kind.ADD:
    expanded += f"ADD({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.MUL:
    expanded += f"MUL({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.MINUS:
    expanded += f"MINUS({expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.POWER:
    expanded += f"POWER({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.ASSIGN:
    expanded += f"ASSIGN({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_ADD:
    expanded += f"ASSIGN_ADD({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_SUB:
    expanded += f"ASSIGN_SUB({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_MUL:
    expanded += f"ASSIGN_MUL({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_DIV:
    expanded += f"ASSIGN_DIV({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_MOD:
    expanded += f"ASSIGN_MOD({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.ASSIGN_POW:
    expanded += f"ASSIGN_POW({expand_tree(tree.name)}, {expand_tree(tree.expr)})"

  elif node_type == TR_Node_Kind.EQUAL:
    expanded += f"EQUAL({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.NEQ:
    expanded += f"NEQ({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.LT:
    expanded += f"LT({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.GT:
    expanded += f"GT({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.LEQ:
    expanded += f"LEQ({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.GEQ:
    expanded += f"GEQ({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.CALL:
    func = expand_tree(tree.func)
    args = ", ".join([expand_tree(arg) for arg in tree.args])
    expanded += f"CALL({func}, ({args}))"

  elif node_type == TR_Node_Kind.PYFUNC_CALL:
    args = ", ".join([expand_tree(arg) for arg in tree.args])
    expanded += f"PYFUNC_CALL({tree.name}, ({args}))"

  elif node_type == TR_Node_Kind.DEF:
    args = ", ".join([expand_tree(arg) for arg in tree.args])
    exprs = ", ".join([expand_tree(expr) for expr in tree.exprs])
    expanded += f"DEF(({args}), ({exprs}))"

  return expanded

def get_expanded_code(program):
  tokens = tr_lexer(program)
  trees = tr_parser(tokens)
  expanded_code = expand_trees(trees)

  return expanded_code

# ---
