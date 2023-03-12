from typing import Callable

def nth(equation: Callable[[float], float], n: int, x: float, h: float=0.00000001):
    if n <= 0:
        return None
    elif n == 1:
        return (equation(x + h) - equation(x)) / h

    return (nth(equation, n - 1, x + h) - nth(equation, n - 1, x)) / h
