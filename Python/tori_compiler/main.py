from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 

from tr_show_tree import show_trees

program = """
f = {(a, b), a+b}; f(1, 2);
"""

tokens = tr_lexer(program)
print(tokens)
trees = tr_parser(tokens)
show_trees(trees)
tori_minus_run(trees)
