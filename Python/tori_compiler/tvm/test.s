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
	call tvm_clr
	push 0
	push 80
	call tvm_copy
	call tvm_print
	mov eax, 0
	pop rbp
	ret
