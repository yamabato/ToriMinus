from tori_test import *

# ---
# ヘルパー関数類

def run_tori_minus_test_code(code):
  evaluator = Evaluator()
  tokens = tr_lexer(code)
  trees = tr_parser(tokens)

  for tree in trees:
    ret = evaluator.eval(tree)

  return get_ret_value(ret)

def get_ret_value(ret):
  ret_kind = ret.kind

  if ret_kind == TR_Value_Kind.num_:
    return float(ret.value)
 
  elif ret_kind == TR_Value_Kind.str_:
    return ret.value
 
  elif ret_kind == TR_Value_Kind.bool_:
    return ret.value == "true"

  elif ret_kind == TR_Value_Kind.non_:
    return None
 
# ---
