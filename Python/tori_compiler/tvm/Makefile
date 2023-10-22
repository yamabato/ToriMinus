.PHONY: test

TVM_FUNCS := print.s clr.s copy.s

tvm: $(TVM_FUNCS) 
	gcc -W -r -nostdlib $(TVM_FUNCS) -o tvm.o

clean:
	rm *.o

test: test.s
	make tvm
	gcc -c test.s
	gcc -o test test.o tvm.o
	./test
