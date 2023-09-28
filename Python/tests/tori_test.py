import os
import sys

sys.path.append(os.path.join(os.getcwd(), "tori_compiler/"))

from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import tr_eval
from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node_Kind 
