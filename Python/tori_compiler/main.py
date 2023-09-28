from tr_lexer import tr_lexer
from tr_parser import tr_parser

from tr_show_tree import show_trees

program = """
pyfunc #print;
1+2;
#print(1+2*3);
f = {(a, b),
      a + b,
};
a = 5;
b = 1 + 2 * 3 * (5+2);
c = f(10*f(1,3), 5);
a += b = c + 2;
#print(f(a+b, c));
#print({(x, y), 
x * y}(1,2));
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
show_trees(trees)
