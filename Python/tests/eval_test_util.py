from tori_test import *

# ---
# ヘルパー関数類

def run_tori_minus_test_code(code):
  tokens = tr_lexer(code)
  trees = tr_parser(tokens)
  ret = tr_eval(trees[0])

  return ret
 
# ---
