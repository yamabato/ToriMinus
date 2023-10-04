from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 

from tr_show_tree import show_trees

program = """
a = 12;
if a == 10{
  #print("a is 10\n");
}
else if a == 2{
  #print("a is 2\n");
  a = 2**2;
}
else{
  #print("???\n");
};
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
show_trees(trees)
tori_minus_run(trees)
