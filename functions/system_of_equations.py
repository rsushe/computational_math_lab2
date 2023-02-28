from typing import Callable
from math import sin, asin

system_of_equations_string: list[str] = [
    "{ -0.3 + 0.1x^2 + 0.2y^2 + x, -0.7 + 0.2x^2 + 0.1xy + y }",
    "{ sin(x) + y - 1, -2x^3 - 4y + 5 }"
]

system_of_equations: list[list[Callable[[float], float]]] = [
    [lambda x, y : -0.3 + 0.1 * x ** 2 + 0.2 * y ** 2 + x, lambda x, y : -0.7 + 0.2 * x ** 2 + 0.1 * x * y + y],
    [lambda x, y : sin(x) + y - 1, lambda x, y : -2 * x ** 3 - 4 * y + 5]
]

derivatives_of_system_of_equations: list[list[Callable[[float], float]]] = [
    [lambda x, y : 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2, lambda x, y : 0.7 - 0.2 * x ** 2 + 0.1 * x * y],
    [lambda x, y : asin(1 - y), lambda x, y : (5 - 2 * x ** 3) / -4]
]