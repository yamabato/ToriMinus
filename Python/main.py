from lexer import lexer

program = """
1 + 2 * 3;
"""

tokens = lexer(program)
print(tokens)
