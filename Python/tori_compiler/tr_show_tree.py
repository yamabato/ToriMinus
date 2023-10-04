from tr_node import TR_Node_Kind

def show_trees(trees):
  for tree in trees:
    print(pretty_node(tree))

def pretty_node(node):
  node_kind = node.kind

  if node_kind == TR_Node_Kind.INT:
    return str(node.value)

  elif node_kind == TR_Node_Kind.DEC:
    return str(node.value)

  elif node_kind == TR_Node_Kind.STR:
    value = node.value.replace("\n", "\\n")
    return f"\"{value}\""

  elif node_kind == TR_Node_Kind.BOOL:
    return f"`{node.value}`"

  elif node_kind == TR_Node_Kind.NON:
    return f"`{node.value}`"

  elif node_kind == TR_Node_Kind.VAR:
    return f"({str(node.value)})"

  elif node_kind == TR_Node_Kind.ADD:
    return f"({pretty_node(node.left)} + {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.SUB:
    return f"({pretty_node(node.left)} - {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.MUL:
    return f"({pretty_node(node.left)} * {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.DIV:
    return f"({pretty_node(node.left)} / {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.MOD:
    return f"({pretty_node(node.left)} % {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.POW:
    return f"({pretty_node(node.left)} ** {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.AND:
    return f"({pretty_node(node.left)} & {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.OR:
    return f"({pretty_node(node.left)} | {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.XOR:
    return f"({pretty_node(node.left)} ^ {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.NOT:
    return f"(!{pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.MINUS:
    return f"(-{pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.POW:
    return f"({pretty_node(node.left)} ** {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.ASSIGN:
    return f"({pretty_node(node.var)} = {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_ADD:
    return f"({pretty_node(node.var)} += {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_SUB:
    return f"({pretty_node(node.var)} -= {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_MUL:
    return f"({pretty_node(node.var)} *= {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_DIV:
    return f"({pretty_node(node.var)} /= {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_MOD:
    return f"({pretty_node(node.var)} %= {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.ASSIGN_POW:
    return f"({pretty_node(node.var)} **= {pretty_node(node.expr)})"

  elif node_kind == TR_Node_Kind.EQUAL:
    return f"({pretty_node(node.left)} == {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.NEQ:
    return f"({pretty_node(node.left)} != {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.LT:
    return f"({pretty_node(node.left)} < {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.GT:
    return f"({pretty_node(node.left)} > {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.LEQ:
    return f"({pretty_node(node.left)} <= {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.GEQ:
    return f"({pretty_node(node.left)} >= {pretty_node(node.right)})"

  elif node_kind == TR_Node_Kind.CALL:
    args = ", ".join([pretty_node(arg) for arg in node.args])
    return f"({pretty_node(node.func)}({args}))"

  elif node_kind == TR_Node_Kind.PYFUNC_CALL:
    args = ", ".join([pretty_node(arg) for arg in node.args])
    return f"({node.name}({args}))"

  elif node_kind == TR_Node_Kind.DEF:
    args = ", ".join([pretty_node(arg) for arg in node.args])
    exprs = ", ".join([pretty_node(expr) for expr in node.exprs])
    return f"({{({args}), ({exprs})}})"

  elif node_kind == TR_Node_Kind.PYFUNC:
    funcs = ", ".join(node.funcs)
    return f"pyfunc {funcs};"

  elif node_kind == TR_Node_Kind.IF:
    return f"if(({pretty_node(node.cond)}){{{';'.join([pretty_node(stmt) for stmt in node.if_stmts])}}}else({{{';'.join([pretty_node(stmt) for stmt in node.else_stmts])}}}))"

  elif node_kind == TR_Node_Kind.WHILE:
    return f"while(({pretty_node(node.cond)}){{{';'.join([pretty_node(stmt) for stmt in node.stmts])}}})"
