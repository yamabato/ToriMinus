	.intel_syntax noprefix
	.globl  main
	.type   main, @function
main:
	endbr64
	push rbp
	mov rbp, rsp
	push 0
	push 10
	push 69
	push 66
	push 65
	mov eax, 0
	call tvm_print
	mov eax, 0
	pop rbp
	ret
