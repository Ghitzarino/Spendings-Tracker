# Simple makefile to easily run the project
PYTHON := python3

run:
	$(PYTHON) code/main.py

clean:
	rm -r plots/*

.PHONY: run