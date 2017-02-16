"""Infix to Postfix Converter

https://www.codewars.com/kata/infix-to-postfix-converter/train/python
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f

Construct a function that, when given a string containing an expression in infix notation,
will return an identical expression in postfix notation.

The operators used will be +, -, *, /, and ^ with standard precedence rules and
left-associativity of all operators but ^.

The operands will be single-digit integers between 0 and 9, inclusive.

Parentheses may be included in the input, and are guaranteed to be in correct pairs.

to_postfix("2+7*5") # Should return "275*+"
to_postfix("3*3/(7+1)") # Should return "33*71+/"
to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
c++ to_postfix("2+7*5") # Should return "275*+" to_postfix("3*3/(7+1)")
# Should return "33*71+/" to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"

You may read more about postfix notation, also called Reverse Polish notation,
here: http://en.wikipedia.org/wiki/Reverse_Polish_notation

"""

ORDERS = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '(': 0,
    ')': 4
}


def to_postfix(infix):
    """Convert infix to postfix

    >>> to_postfix("2+7*5")
    '275*+'
    >>> to_postfix("3*3/(7+1)")
    '33*71+/'
    >>> to_postfix("5+(6-2)*9+3^(7-1)")
    '562-9*+371-^+'
    >>> to_postfix("(5-4-1)+9/5/2-7/1/7")
    '54-1-95/2/+71/7/-'

    """
    stack = []
    result = []
    for c in infix:
        if c.isdigit():
            result.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and ORDERS[stack[-1]] >= ORDERS[c]:
                    result.append(stack.pop())
            stack.append(c)

    if stack:
        result.extend(reversed(stack))
    return ''.join(result)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
