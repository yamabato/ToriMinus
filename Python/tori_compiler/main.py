from tr_lexer import tr_lexer
from tr_parser import tr_parser

from tr_show_tree import show_trees

program = """
1+2;
"""

program = "f(\"abc\");"

tokens = tr_lexer(program)
trees = tr_parser(tokens)
show_trees(trees)
