from typing import Callable
from math import sin, cos

class Equation:
    itself: Callable[[float], float]
    string_representation: str

    def __init__(self, itself: Callable[[float], float], string_representation: str) -> None:
        self.itself = itself
        self.string_representation = string_representation


first_equation = Equation(lambda x: -1.4 * x ** 3 - 0.9 * x ** 2 + 10.67 * x - 2.34, "-1.4x^3 - 0.9x^2 + 10.67x - 2.34")
second_equation = Equation(lambda x: x ** 3 - 3 * x + 1, "x^3 - 3x + 1")
third_equation = Equation(lambda x: sin(x) - cos(x) + 1.5 * x, "sin(x) - cos(x) + 1.5x")

equations: list[Equation] = [
    first_equation,
    second_equation,
    third_equation
]