from tr_lexer import tr_lexer

program = """
a()
"""

tokens = tr_lexer(program)
print(tokens)
