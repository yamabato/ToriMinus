from tr_lexer import tr_lexer

program = """
~ピラミッドを表示する~

pyfunc #print,#loop,#int;

~Nは段数,nはloop用の変数~
N=10;
n=0;

#loop
(
    n+=1,
    n<N,
    #print(
        (" "*(N-n)+"*"*(n*2+1))
    )
);
~pythonの15倍の時間~
"""

tokens = tr_lexer(program)
print(tokens)
