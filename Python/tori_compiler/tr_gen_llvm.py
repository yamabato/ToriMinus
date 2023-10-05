import re
import sys
import time
import copy
import random

from tr_node import TR_Node_Kind
from tr_value import TR_Value, TR_Value_Kind
from tr_show_tree import pretty_node 

# ---
# 定数等の設定

INIT_VALUE = {
  "i32": "0"
}

UNARY_OPERATORS = [
  TR_Node_Kind.MINUS,
  TR_Node_Kind.NOT,
]

ARITHMETIC_OPERATORS = [
  TR_Node_Kind.ADD,
  TR_Node_Kind.SUB,
  TR_Node_Kind.MUL,
  TR_Node_Kind.DIV,
  TR_Node_Kind.MOD,
  TR_Node_Kind.POW
]

LOGICAL_OPERATORS = [
  TR_Node_Kind.AND,
  TR_Node_Kind.OR,
  TR_Node_Kind.XOR,
]

ASSIGNMENT_OPERATORS = [
  TR_Node_Kind.ASSIGN,
  TR_Node_Kind.ASSIGN_ADD,
  TR_Node_Kind.ASSIGN_SUB,
  TR_Node_Kind.ASSIGN_MUL,
  TR_Node_Kind.ASSIGN_DIV,
  TR_Node_Kind.ASSIGN_MOD,
  TR_Node_Kind.ASSIGN_POW,
  TR_Node_Kind.ASSIGN_AND,
  TR_Node_Kind.ASSIGN_OR,
  TR_Node_Kind.ASSIGN_XOR,
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

class LLVM_Generator:
  def __init__(self, level=0):
    self.level = 0

    self.func_def_code = []
    self.global_var_dec_code = []

    self.local_var_dec_code = []
    self.main_code = []

    self.local_var_number = 1
    self.global_var_number = 0

  def gen(self, trees):
    for tree in trees:
      self.gen_node_code(tree)

    return self.func_def_code, self.global_var_dec_code, self.local_var_dec_code, self.main_code

  def gen_node_code(self, node):
    node_kind = node.kind
    
    ret_var_name = ""
    if node_kind == TR_Node_Kind.INT:
      ret_var_name = self.gen_int(node)

    elif node_kind in ASSIGNMENT_OPERATORS:
      ret_var_name = self.gen_assign(node)

    else:
      print("ERROR-EVAL:", node_kind)
      sys.exit()

    return ret_var_name

  # ---
  
  def get_local_var_number(self):
    lvn = self.local_var_number
    self.local_var_number += 1
    return lvn

  def get_global_var_number(self):
    gvn = self.global_var_number
    self.global_var_number += 1
    return gvn

  def gen_global_var_dec_code(self, var_ident, var_type, var_value=""):
    if var_value == "": var_value = INIT_VALUE[var_type]
    self.global_var_dec_code.append(f"@{var_ident} = global {var_type} {var_value}")
    return f"@{var_ident}"

  def gen_local_var_dec_code(self, var_ident, var_type):
    self.local_var_dec_code.append(f"%{var_ident} = alloca {var_type}")
    return f"%{var_ident}"

  def gen_var_assign_code(self, var_name, var_type, var_value):
    self.main_code.append(f"store {var_type} {var_value}, {var_type}* {var_name}")

  def gen_tmp_var_assign_code(self, var_type, var_value):
    lvn = self.get_local_var_number()
    name = self.gen_local_var_dec_code(lvn, var_type)
    self.gen_var_assign_code(name, var_type, var_value)

    return name

  def gen_load_value_code(self, var_name, var_type):
    lvn = self.get_local_var_number()
    name = f"%{lvn}"

    self.main_code.append(f"{name} = load {var_type}, {var_type}* {var_name}")
    return name

  # ---

  def gen_int(self, node):
    name = self.gen_tmp_var_assign_code("i32", node.value)
    return name

  def gen_assign(self, node):
    ident = node.var.value
    expr = node.expr

    value_var_name = self.gen_node_code(expr)
    if self.level == 0:
      name = self.gen_global_var_dec_code(ident, "i32")
    else:
      name = self.gen_local_var_dec_code(ident, "i32")
    
    value_loaded_var = self.gen_load_value_code(value_var_name, "i32")
    self.gen_var_assign_code(name, "i32", value_loaded_var)

# ---

def tori_minus_gen_llvm(trees):
  generator = LLVM_Generator()
  func_def_code, global_var_dec_code, local_var_dec_code, main_code = generator.gen(trees)

  func_def = "\n".join(func_def_code)
  global_var_dec = "\n".join(global_var_dec_code)
  local_var_dec = "\n  ".join(local_var_dec_code)
  main = "\n  ".join(main_code) + "\n  ret i32 0"
  
  print(func_def)
  print(global_var_dec)
  print("define i32 @main() {\n  " + local_var_dec + "\n  " + main + "\n}")

# ---
