from tr_lexer import tr_lexer

program = """
123.456"""

tokens = tr_lexer(program)
print(tokens)
