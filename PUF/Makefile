CC = g++
CFLAGS = -Wall -O2

build: bin bin/main.o
	$(CC) bin/*.o -o bin/main.out $(CFLAGS)

bin/main.o:
	$(CC) -c src/main.cpp -o bin/main.o $(CFLAGS)

bin:
	mkdir bin

clean:
	rm -rfv bin/

rebuild: clean build
