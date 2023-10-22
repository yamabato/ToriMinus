  .intel_syntax noprefix
  .text
  .globl tvm_char
  .type tvm_char, @function
tvm_char:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
  pop rax
  mov edi, eax
  call putchar@PLT
  push r15					#ripの値をスタックに戻す
  ret
