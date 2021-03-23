Calculator
----------

This project implements a simple calculator in Python. It includes a simple lexer and expression evaluator.

Here is an example usage:

```
python3 cacl.py
Enter expression:2*(1+2)
6.0
```

Tests can be run using:

```
make test
```

or

```
python3 -m doctest calc.py
```

There is a small bug present in the program currently. Find the bug, and adjust the program so that this class of bugs can be easily detected and fixed in the future. Hint: you might want to look at `Enum`.
