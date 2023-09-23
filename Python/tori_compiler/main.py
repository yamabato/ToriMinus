from tr_lexer import tr_lexer

program = """
== !=
"""

tokens = tr_lexer(program)
print(tokens)
