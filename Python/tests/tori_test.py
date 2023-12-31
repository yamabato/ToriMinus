import os
import sys

sys.path.append(os.path.join(os.getcwd(), "tori_compiler/"))

from tr_lexer import tr_lexer
from tr_parser import tr_parser
from tr_run import Evaluator 
from tr_token import TR_Token, TR_Token_Kind
from tr_node import TR_Node_Kind 
from tr_value import TR_Value_Kind 
