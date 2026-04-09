#
# This is a makefile for lab1part1.  It assumes your part1 file is named
# lab1.c 
#

CC = gcc

GCCFLAGS = -fpcc-struct-return
CFLAGS = -g

INCLUDE = -I/usr/local/include

LDLIBS =  -lX11 

LDFLAGS = -L/usr/local/lib

myHello: myHello.c
	$(CC) $(GCCFLAGS) $(INCLUDE) $(CFLAGS) -DUNIX -DX11 \
            myHello.c \
            $(LDFLAGS) $(LDLIBS) -o myHello

