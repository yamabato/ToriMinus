import os
import sys

from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 
from tr_show_tree import show_trees

show_tree_flg = False
program_loaded = False

program = ""
if __name__ == "__main__":
  args = sys.argv[1:]

  for arg in args:
    if os.path.isfile(arg):
      with open(arg, mode="r") as f:
        program = f.read()
        program_loaded = True

    elif arg == "-s": show_tree_flg = True

  if not program_loaded:
    print("ファイルを指定してください")

  tokens = tr_lexer(program)

  trees = tr_parser(tokens)
  if show_tree_flg: show_trees(trees)

  tori_minus_run(trees)
