all: program

program: main.c file1.o file2.o
	cc -g -Wall main.c file1.o file2.o -o program

file1.o: file1.h
	cc -g -Wall -c file1.h -o file1.o

file2.o: file2.h
	cc -g -Wall -c file2.h -o file2.o

clean:
	rm -f *.o program
