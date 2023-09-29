from tori_test import *

# ---
# ヘルパー関数類

def run_tori_minus_test_code(code):
  evaluator = Evaluator()
  tokens = tr_lexer(code)
  trees = tr_parser(tokens)

  for tree in trees:
    ret = evaluator.eval(tree)

  return ret
 
# ---
