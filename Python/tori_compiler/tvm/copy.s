  .intel_syntax noprefix
  .text
  .globl tvm_copy
  .type tvm_copy, @function
tvm_copy:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
	pop r14						#コピーしたい値をr14に移動
	push r14
	push r14					#コピー
  push r15					#ripの値をスタックに戻す
  ret
