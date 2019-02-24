1 compile two file add.c and sub.c
gcc -fPIC -c add.c

PIC-postion independnt code

2 gcc -shared -o libbasic.so add.o sub.o

3 gcc -c demo.c

4 gcc -o demo demo.o libbasic.so

5 sudo mv libbasic.so /usr/lib/

6 sudo ldconfig

7 ./demo
