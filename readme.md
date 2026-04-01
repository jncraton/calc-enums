# Calculator

This project implements a simple calculator in Python. It includes a simple lexer and expression evaluator.

## Learning Outcomes

After completing this lab, learners will be able to:

1. Diagnose bugs in existing software
2. Use Python `Enum` to reduce surface area for bugs

## Usage

```
python3 cacl.py
Enter expression:2*(1+2)
6.0
```
## Testing

Tests can be run using:

```
make test
```

or

```
python3 -m doctest calc.py
```

## Task

There is a small bug present in the program currently. Find the bug, and adjust the program to use an `Enum` so that this class of bugs can be easily detected and fixed in the future.
