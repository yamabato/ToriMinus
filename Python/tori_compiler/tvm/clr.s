  .intel_syntax noprefix
  .text
  .globl tvm_clr
  .type tvm_clr, @function
tvm_clr:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
	mov rsp, rbp
  push r15					#ripの値をスタックに戻す
  ret
