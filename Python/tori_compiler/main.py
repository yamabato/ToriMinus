from tr_lexer import tr_lexer
from tr_parser import tr_parser

program = """
1+2;
"""

program = "a+=b=2"

tokens = tr_lexer(program)
trees = tr_parser(tokens)
print(trees)
