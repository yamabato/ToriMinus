  .intel_syntax noprefix
  .text
  .globl tvm_print
  .type tvm_print, @function
tvm_print:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
  tvm_print_lp:
  pop rax
  mov edi, eax
  cmp rdi, 0
  je tvm_print_fin	#次の文字が\x00なら終了
  call putchar@PLT
  jmp tvm_print_lp	#繰り返してputchar
  tvm_print_fin:
  push r15					#ripの値をスタックに戻す
  ret
