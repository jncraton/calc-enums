all: test

test:
	python3 -m doctest calc.py

clean:
	rm -rf __pycache__
