import operator
import re


def tokenize(text):
    """
    Tokenize an expression

    >>> len(list(tokenize("1+2")))
    3

    >>> next(tokenize("1-2"))[1]
    '1'
    """

    tokens = {
        "LITERAL": "([\d\.]+)",
        "OPERATOR": "([\+\-\*/])",
        "OPEN": "(\()",
        "CLOSE": "(\))",
    }

    while text:
        for name, regexp in tokens.items():
            m = re.match(regexp, text)

            if m:
                text = text[len(m.group(0)):]
                yield name, m.group(1)
                break
        else:
            raise Exception(f"Invalid token here>{text[:10]}")


def evaluate(tokens):
    """
    Evaluates an iterator of tokens

    >>> evaluate(tokenize(""))
    0.0
    
    >>> evaluate(tokenize("1.0"))
    1.0
    
    >>> evaluate(tokenize("1+2+3+4+5"))
    15.0

    >>> evaluate(tokenize("5-1-2"))
    2.0

    >>> evaluate(tokenize("2*(3*(1+2)+1)"))
    20.0

    >>> evaluate(tokenize("4*(7*(3-1)-2)/2"))
    24.0
    """

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    result = 0.0
    op = "+"

    for name, value in tokens:
        if name == "OPEN":
            value = evaluate(tokens)
        if name in ("LITERAL", "OPEN"):
            result = operations[op](result, float(value))
        elif name == "OPERATION":
            op = value
        elif name == "CLOSE":
            return result

    return result


if __name__ == "__main__":
    print(evaluate(tokenize(input("Enter expression:"))))
