.PHONY: test

tvm: print.s
	gcc -W -r -nostdlib  print.s -o tvm.o

clean:
	rm *.o

test: test.s
	make tvm
	gcc -c test.s
	gcc -o test test.o tvm.o
	./test
