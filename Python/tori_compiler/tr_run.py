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

def bool_to_tr_bool(value):
  if value: return "true"
  return "false"

# ---

env_global = {}
class Evaluator:
  def __init__(self, level=0):
    self.env = {}
    self.level = level 

    self.pyfunc_table = {
      "#if": self.tr_pf_if,
      "#while": self.tr_pf_while,
      "#for": self.tr_pf_for,
      "#print": self.tr_pf_print,
      "#input": self.tr_pf_input,
      "#len": self.tr_pf_len,
      "#index": self.tr_pf_index,
      "#to_num": self.tr_pf_to_num,
      "#to_str": self.tr_pf_to_str,
      "#to_bool": self.tr_pf_to_bool,
      "#exit": self.tr_pf_exit,
      "#set_global": self.tr_pf_set_global,
      "#del": self.tr_pf_del,
      "#type": self.tr_pf_type,
      "#time": self.tr_pf_time,
      "#rand": self.tr_pf_rand,
    }

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

    elif node_kind in UNARY_OPERATORS:
      ret = self.eval_unary(node)

    elif node_kind in ARITHMETIC_OPERATORS:
      ret = self.eval_arithemetic_operation(node)

    elif node_kind in LOGICAL_OPERATORS:
      ret = self.eval_logical_operation(node)

    elif node_kind in ASSIGNMENT_OPERATORS:
      ret = self.eval_assignment_operation(node)

    elif node_kind in COMPARISON_OPERATORS:
      ret = self.eval_comparison_operation(node)

    elif node_kind == TR_Node_Kind.DEF:
      ret = self.eval_define_function(node)

    elif node_kind == TR_Node_Kind.CALL:
      ret = self.eval_call_function(node)

    elif node_kind == TR_Node_Kind.PYFUNC_CALL:
      ret = self.eval_pyfunc_call(node)

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
    ret = TR_Value()

    if node.kind == TR_Node_Kind.MINUS:
      value = self.eval(node.right)
      if value.kind == TR_Value_Kind.num_:
        ret.kind = TR_Value_Kind.num_
        ret.value = -value.value
      else:
        print("ERROR")
        sys.exit

    elif node.kind == TR_Node_Kind.NOT:
      value = self.eval(node.right)
      if value.kind == TR_Value_Kind.bool_:
        ret.kind = TR_Value_Kind.bool_
        ret.value = bool_to_tr_bool(not value)
      else:
        print("ERROR")
        sys.exit()

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

  def eval_logical_operation(self, node):
    left = self.eval(node.left)
    right = self.eval(node.right)

    left_kind = left.kind
    right_kind = right.kind

    left_value = BOOL_VALUE_TABLE[left.value]
    right_value = BOOL_VALUE_TABLE[right.value]

    oper = node.kind

    if left_kind != TR_Value_Kind.bool_ or right_kind != TR_Value_Kind.bool_:
      print("ERROR")
      sys.exit()
   
    ret = TR_Value()
    ret.kind = TR_Value_Kind.bool_
    if oper == TR_Node_Kind.AND:
      ret.value = left_value & right_value 
    elif oper == TR_Node_Kind.OR:
      ret.value = left_value | right_value 
    elif oper == TR_Node_Kind.XOR:
      ret.value = left_value ^ right_value 
    
    ret.value = bool_to_tr_bool(ret.value)
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

  def eval_define_function(self, node):
    args = node.args
    exprs = node.exprs

    ret = TR_Value()
    ret.kind = TR_Value_Kind.func_
    ret.args = args
    ret.exprs = exprs

    return ret

  def eval_call_function(self, node):
    func = self.eval(node.func)
    func_args = func.args
    func_exprs = func.exprs

    args = node.args

    func_evaluator = Evaluator(self.level+1)
    func_evaluator.env = copy.deepcopy(self.env)

    if len(func_args) != len(args):
      print("ERROR")
      sys.exit()

    for var, expr in zip(func_args, args):
      func_evaluator.assign(var, func_evaluator.eval(expr))
      
    ret = TR_Value()
    ret.kind = TR_Value_Kind.non_
    for expr in func_exprs:
      ret = func_evaluator.eval(expr)

    return ret

  def eval_pyfunc_call(self, node):
    name = node.name
    args = node.args

    if name not in self.pyfunc_table:
      print("ERRO")
      sys.exit()
    
    ret = self.pyfunc_table[name](args)
    return ret

  # ---
  
  def assign(self, var, value):
    name = var.value
    self.env[name] = value
    if self.level == 0:
      env_global[name] = value

  def pretty_value(self, value):
    value_kind = value.kind
    if value_kind == TR_Value_Kind.num_:
      return str(value.value)
    elif value_kind == TR_Value_Kind.str_:
      return value.value
    elif value_kind == TR_Value_Kind.bool_:
      return f"`{value.value}`"
    elif value_kind == TR_Value_Kind.non_:
      return "`non`"
    elif value_kind == TR_Value_Kind.func_:
      exprs = value.exprs
      exprs_ = ", ".join(map(pretty_node, exprs))

      args = value.args
      args_ = ", ".join(map(pretty_node, args))

      return f"{{({args_}), ({exprs_})}}"

  def eval_args(self, args):
    args_evaluated = [self.eval(arg) for arg in args]
    return args_evaluated

  def check_pyfunc_args_count(self, args, length):
    if len(args) not in length:
      print("ERROR")
      sys.exit()

  def check_pyfunc_args_type(self, args, types):
    for arg, t in zip(args, types):
      if arg.kind != t:
        print("ERROR")
        sys.exit()

  def is_num(self, str_):
    return bool(re.fullmatch("[+-]?(\d+\.?\d*|\d*\.\d+)", str_))

  def convert_str_to_num(self, str_):
    if "." in str_: return float(str_)
    return int(str_)

  # ---
  # pyfunc

  def tr_pf_if(self, args):
    self.check_pyfunc_args_count(args, [3])

    cond = self.eval(args[0])
    if cond.kind != TR_Value_Kind.bool_:
      print("ERROR")
      sys.exit()

    if BOOL_VALUE_TABLE[cond.value]:
      ret = self.eval(args[1])
    else:
      ret = self.eval(args[2])

    return ret

  def tr_pf_while(self, args):
    self.check_pyfunc_args_count(args, [2])

    while True:
      cond = self.eval(args[0])
      if cond.kind != TR_Value_Kind.bool_:
        print("ERROR")
        sys.exit()

      if not BOOL_VALUE_TABLE[cond.value]: break

      ret = self.eval(args[1])

    return ret

  def tr_pf_for(self, args):
    self.check_pyfunc_args_count(args, [4])

    self.eval(args[0])
    while True:
      ret = self.eval(args[3])

      self.eval(args[2])
      cond = self.eval(args[1])
      if cond.kind != TR_Value_Kind.bool_:
        print("ERROR")
        sys.exit()
      if not BOOL_VALUE_TABLE[cond.value]: break

    return ret

  def tr_pf_print(self, args):
    args = self.eval_args(args)
    output = [] 
    for arg in args:
      output.append(self.pretty_value(arg))

    sys.stdout.write(" ".join(output))
    sys.stdout.flush()

    ret = TR_Value()
    ret.kind = TR_Value_Kind.non_
    return ret

  def tr_pf_input(self, args):
    self.check_pyfunc_args_count(args, [0])

    ret = TR_Value()
    ret.kind = TR_Value_Kind.str_
    ret.value = sys.stdin.readline()[:-1]

    return ret

  def tr_pf_len(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [1])
    self.check_pyfunc_args_type(args, [TR_Value_Kind.str_])

    arg = args[0] 
    ret = TR_Value()
    ret.kind = TR_Value_Kind.num_
    ret.value = len(arg.value)
    return ret

  def tr_pf_index(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [2])
    self.check_pyfunc_args_type(args, [TR_Value_Kind.str_, TR_Value_Kind.num_])

    text = args[0]
    ind = args[1]
    
    if ind.kind != TR_Value_Kind.num_:
      print("ERROR")
      sys.exit
    if len(text.value) <= ind.value or ind.value < 0:
      print("ERROR")
      sys.exit()
    if int(ind.value) != ind.value:
      print("ERROR")
      sys.exit()
    
    ret = TR_Value()
    ret.kind = TR_Value_Kind.str_
    ret.value = text.value[int(ind.value)]

    return ret
 
  def tr_pf_to_num(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [1])
    self.check_pyfunc_args_type(args, [TR_Value_Kind.str_])

    arg = args[0]
    if self.is_num(arg.value):
      ret = TR_Value()
      ret.value = self.convert_str_to_num(arg.value)
      ret.kind = TR_Value_Kind.num_
    else:
      print("ERROR")
      sys.exit()

    return ret

  def tr_pf_to_str(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [1])

    arg = args[0]
    arg_kind = arg.kind

    ret = TR_Value()
    if arg_kind == TR_Value_Kind.num_:
      ret.value = str(arg.value)
    elif arg_kind == TR_Value_Kind.str_:
      ret.value = arg.value
    elif arg_kind == TR_Value_Kind.bool_:
      ret.value = f"`{arg.value}`"
    elif arg_kind == TR_Value_Kind.non_:
      ret.value = "`non`"
    elif arg_kind == TR_Value_Kind.func_:
      ret.value = self.pretty_value(arg)

    ret.kind = TR_Value_Kind.str_
    return ret

  def tr_pf_to_bool(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [1])

    arg = args[0]
    arg_kind = arg.kind

    ret = TR_Value()
    if arg_kind == TR_Value_Kind.num_:
      value = arg.value != 0
    elif arg_kind == TR_Value_Kind.str_:
      value = arg.value != ""
    elif arg_kind == TR_Value_Kind.bool_:
      value = BOOL_VALUE_TABLE[arg.value]
    elif arg_kind == TR_Value_Kind.non_:
      value = False
    elif arg_kind == TR_Value_Kind.func_:
      value = True
    
    ret.value = bool_to_tr_bool(value)
    ret.kind = TR_Value_Kind.bool_
    return ret


  def tr_pf_exit(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [0, 1])
    
    code = 0
    if len(args) == 1:
      self.check_pyfunc_args_type(args, [TR_Value_Kind.num_])
      code = args[0].value

    sys.exit(code)

  def tr_pf_set_global(self, args):
    self.check_pyfunc_args_count(args, [2])

    var = args[0]
    val = self.eval(args[1])

    if var.kind != TR_Node_Kind.VAR:
      print("ERROR")
      sys.exit()

    self.assign(var, val)

    return val

  def tr_pf_del(self, args):
    self.check_pyfunc_args_count(args, [1])

    arg = args[0]
    if arg.kind != TR_Node_Kind.VAR:
      print("ERROR")
      sys.exit()

    if arg.value not in self.env:
      print("ERROR")
      sys.exit()

    del self.env[arg.value]    
    if self.level == 0:
      del env_global[arg.value]

    ret = TR_Value()
    ret.kind = TR_Value_Kind.non_
    return ret

  def tr_pf_type(self, args):
    args = self.eval_args(args)
    self.check_pyfunc_args_count(args, [1])

    arg = args[0]
    arg_kind = arg.kind

    ret = TR_Value()
    ret.kind = TR_Value_Kind.str_
    if arg_kind == TR_Value_Kind.num_:
      ret.value = "num"
    elif arg_kind == TR_Value_Kind.str_:
      ret.value = "str"
    elif arg_kind == TR_Value_Kind.bool_:
      ret.value = "bool"
    elif arg_kind == TR_Value_Kind.non_:
      ret.value = "non"
    elif arg_kind == TR_Value_Kind.func_:
      ret.value = "func"

    return ret

  def tr_pf_time(self, args):
    self.check_pyfunc_args_count(args, [0])
  
    ret = TR_Value()
    ret.kind = TR_Value_Kind.num_
    ret.value = time.time()
  
    return ret

  def tr_pf_rand(self, args):
    self.check_pyfunc_args_count(args, [0])

    ret = TR_Value()
    ret.kind = TR_Value_Kind.num_
    ret.value = random.random()
  
    return ret

# ---

def tori_minus_run(trees):
  evaluator = Evaluator()
  for tree in trees:
    value = evaluator.eval(tree)
    sys.stdout.flush()

# ---
