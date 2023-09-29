from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tori_minus_run 

from tr_show_tree import show_trees

program = """
ret = #if(1==2, 2**3, 3**4);
#print(ret, "\n");
n = 0;
#while(n<10, n={(), #print(#to_str(n) + "\n"), n+=1}());
"""

tokens = tr_lexer(program)
trees = tr_parser(tokens)
tori_minus_run(trees)
