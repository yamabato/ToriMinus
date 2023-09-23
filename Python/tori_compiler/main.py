from tr_lexer import tr_lexer

program = """
1"""

tokens = tr_lexer(program)
print(tokens)
