"""Implementations of a few common math functions."""

def fact(n):
    """Factorial function. Returns ``n*(n-1)*(n-2)*...*1``"""
    result = n
    for i in range(n-1, 0, -1):
        result *= i
    return result

def pow(b, n):
    """Power function. Returns :literal:`b`:sup:`n`. Useless wrapper for
    ``b**n``.
    """
    return b ** n

def circle_area(r):
    """Calculates the area of a circle as ``PI*r^2``. Assumes that
    ``PI=3.1415``.
    """
    return 3.1415 * r * r
