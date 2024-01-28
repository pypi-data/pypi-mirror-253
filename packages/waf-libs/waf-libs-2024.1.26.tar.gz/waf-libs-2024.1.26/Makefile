DIST := dist/*
CC := gcc
SHELL := /bin/bash

PYTHON := python3
PIP := pip3
SETUP_PY = setup.py

SUDO := /usr/bin/sudo

PIP_ARGS =
ifneq (,$(wildcard /etc/debian_version))
	PIP_ARGS = --break-system-packages
endif

all: install

.PHONY: test install clean full-install

clean:
	$(SUDO) rm -rfv **/*.pyc **/__pycache__ **/**/__pycache__ build dist **/*.egg-info

test: clean
	$(PYTHON) $(SETUP_PY) test

full-install: clean test install

install: clean
	$(PIP) install --editable . $(PIP_ARGS)

user: clean
	$(PIP) install --editable . --user

req:
	$(PIP) install --requirement requirements.txt

dev:
	$(PIP) install --requirement requirements-dev.txt --requirement requirements.txt

build: clean
	$(PYTHON) -m build

upload: build
	$(PYTHON) -m twine upload --repository pypi $(DIST)

check:
	twine check $(DIST)
