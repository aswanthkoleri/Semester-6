1 gcc -c add.c
2 gcc -c sub.c
3 ar rs libbasic.a add.o sub.o
4 gcc -c demo.c
5 gcc -o demo demo.o libbasic.a
6 ./demo
