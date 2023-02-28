from typing import Callable
from math import sin, cos

equations_string: list[str] = [
    "-1.4x^3 - 0.9x^2 + 10.67x - 2.34",
    "x^2 - 2x + 1",
    "sin(x) - cos(x) + 1.5x"
]

equations: list[Callable[[float], float]] = [
    lambda x: -1.4 * x ** 3 - 0.9 * x ** 2 + 10.67 * x - 2.34,
    lambda x: x ** 2 - 2 * x + 1,
    lambda x: sin(x) - cos(x) + 1.5 * x
]

derivatives_of_equations: list[Callable[[float], float]] = [
    lambda x: -4.2 * x ** 2 - 1.8 * x + 10.67,
    lambda x: 2 * x - 2,
    lambda x: cos(x) + sin(x) + 1.5
]