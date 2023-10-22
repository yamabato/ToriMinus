  .intel_syntax noprefix
  .text
  .globl tvm_input
  .type tvm_input, @function
tvm_input:
	endbr64
  pop r15						#スタックトップのripの値をr15に退避
	push 0						#文字列の末端
	tvm_input_lp:
	call  getchar@PLT	#文字入力を受付
	push rax
	cmp rax, 10
	jne tvm_input_lp	#改行されたら終了
  push r15					#ripの値をスタックに戻す
  ret
