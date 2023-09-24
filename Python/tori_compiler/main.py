from tr_lexer import tr_lexer

program = """
1+2;
"""

tokens = tr_lexer(program)
tree = tr_parser(program)
print(tokens)
print(tree)
