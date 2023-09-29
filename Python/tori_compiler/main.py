from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 

from tr_show_tree import show_trees

program = """
#print("age: ");
age = #input();
#print(#to_str(age) + "歳\n");
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
tori_minus_run(trees)
