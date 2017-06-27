#SHELL := /bin/bash

CODE_DIR=build/code
PWD=$(shell pwd)
STATUS=0

all:  build run-py-tests

init: 
	./init.sh

build: init
	make -f tangle-make -k all

run-py-tests:
	export PYTHONPATH=${PWD}/${CODE_DIR}; cd ${PWD}/${CODE_DIR}; python -m unittest discover

clean:	
	make -f tangle-make clean
