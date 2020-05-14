CC = gcc
CFLAGS = -Wall -std=gnu90

build: bin bin/main.o
	$(CC) bin/*.o -o bin/main.out $(CFLAGS)

bin/main.o:
	$(CC) -c src/main.c -o bin/main.o $(CFLAGS)

bin:
	mkdir bin

clean:
	rm -rfv bin/

rebuild: clean build
