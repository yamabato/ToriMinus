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

  elif node_type == TR_Node_Kind.ADD:
    expanded += f"ADD({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.MUL:
    expanded += f"MUL({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.MINUS:
    expanded += f"MINUS({expand_tree(tree.right)})"

  elif node_type == TR_Node_Kind.POWER:
    expanded += f"POWER({expand_tree(tree.left)}, {expand_tree(tree.right)})"

  return expanded

def get_expanded_code(program):
  tokens = tr_lexer(program)
  trees = tr_parser(tokens)
  expanded_code = expand_trees(trees)

  return expanded_code

# ---
