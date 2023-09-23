from tr_lexer import tr_lexer

program = """
"123.4561abc_"
"""

tokens = tr_lexer(program)
print(tokens)
