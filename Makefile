# Simple makefile to easily run the project
PYTHON := python3

run:
	$(PYTHON) code/main.py

.PHONY: run