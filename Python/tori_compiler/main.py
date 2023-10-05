from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 
from tr_gen_llvm import tori_minus_gen_llvm 

from tr_show_tree import show_trees

program = """
x = 1;
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
#show_trees(trees)
#tori_minus_run(trees)
tori_minus_gen_llvm(trees)
