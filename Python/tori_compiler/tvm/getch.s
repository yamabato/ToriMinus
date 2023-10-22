  .intel_syntax noprefix
  .text
  .globl tvm_getch
  .type tvm_getch, @function
tvm_getch:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
	call  getchar@PLT
	push rax
  push r15					#ripの値をスタックに戻す
  ret
