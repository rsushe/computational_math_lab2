from typing import Callable
from math import sin, asin

class SystemOfEquations:
    itself: list[Callable[[float], float]]
    itself_with_expessed_x: list[Callable[[float], float]]
    string_representation: str

    def __init__(self, itself: list[Callable[[float], float]], itself_with_expessed_x: list[Callable[[float], float]], string_representation: str) -> None:
        self.itself = itself
        self.itself_with_expessed_x = itself_with_expessed_x
        self.string_representation = string_representation


first_system_of_equations = SystemOfEquations( [lambda x, y : -0.3 + 0.1 * x ** 2 + 0.2 * y ** 2 + x, 
                                                lambda x, y : -0.7 + 0.2 * x ** 2 + 0.1 * x * y + y],
                                                [lambda x, y: 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2,
                                                 lambda x, y: 0.7 - 0.2 * x ** 2 - 0.1 * x * y],
                                                "{ -0.3 + 0.1x^2 + 0.2y^2 + x, -0.7 + 0.2x^2 + 0.1xy + y }")
second_system_of_equations = SystemOfEquations([lambda x, y : x + y ** 2 - 4, 
                                                lambda x, y : -2 * x ** 3 - 4 * y + 5],
                                                [lambda x, y: 4 - y ** 2,
                                                 lambda x, y: (5 - 2 * x ** 3) / 4],
                                                "{ x + y^2 - 4, -2x^3 - 4y + 5 }")

equations: list[SystemOfEquations] = [
    first_system_of_equations,
    second_system_of_equations,
]