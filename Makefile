.PHONY: run test format lint check-vuln install

install:
	pip install -r requirements.txt

run:
	python main.py

test:
	python -m doctest main.py -v
	pytest -v

format:
	black .

lint:
	flake8 .

check-vuln:
	safety check -r requirements.txt