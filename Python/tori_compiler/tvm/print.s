  .intel_syntax noprefix
  .text
  .globl  print
  .type   print, @function
tvm_print:
  pop r10           ;rbpの値をr10に退避
  tvm_print_lp:
  pop rax           
  mov edi, eax
  cmp rdi, 0        
  je tvm_print_fin  ;次の文字が\x00なら終了
  call putchar@PLT
  jmp tvm_print_lp  ;繰り返してputchar
  tvm_print_fin:
  push r10          ;rbpの値をスタックに戻す
  ret
