	.intel_syntax noprefix
	.globl  main
	.type   main, @function
main:
	endbr64
	push rbp
	mov rbp, rsp
	push 0
	call tvm_getch
	call tvm_print
	mov eax, 0
	pop rbp
	ret
