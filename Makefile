PYTHON = python3

.PHONY: install test run

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest -v test_gerador.py

run:
	$(PYTHON) gerador_senhas.py
