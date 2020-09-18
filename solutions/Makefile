CFLAGS=-Wall -g
CSHARED=-fPIC -shared

all: 0344 1323 0136 0169

0344:
	gcc $(CSHARED) -o 0344-reverse-string/reverse-string.so 0344-reverse-string/0344.c
1323:
	gcc $(CSHARED) -o 1323-maximum-69-number/maximum-69-number.so 1323-maximum-69-number/1323.c
0136:
	gcc $(CSHARED) -o 0136-single-number/single-number.so 0136-single-number/0136.c
0169:
	gcc $(CSHARED) -o 0169-majority-element/majority-element.so 0169-majority-element/0169.c


clean:
	rm -f 0344-reverse-string/reverse-string.so
	rm -f 1323-maximum-69-number/maximum-69-number.so
	rm -f 0136-single-number/single-number.so
	rm -f 0169-majority-element/majority-element.so
