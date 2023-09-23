from lexer import lexer

program = """
123+ 2.3 * 3;
"""

tokens = lexer(program)
print(tokens)
