from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 

from tr_show_tree import show_trees

program = """
#print(#to_str({(a, b),a**b, #print(a+b)})*2, "\n");
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
tori_minus_run(trees)
