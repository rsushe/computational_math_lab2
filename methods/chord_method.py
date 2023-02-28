from typing import Callable

def solve_equation(equation: Callable[[float], float], interval: list[float], accuracy: float):
    a: float = interval[0]
    b: float = interval[1]

    current_x: float = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))

    current_iteration: int = 1
    max_iteration: int = 1000

    while abs(equation(current_x)) > accuracy and current_iteration < max_iteration:

        if equation(a) * equation(current_x) > 0:
            a = current_x
        else:
            b = current_x
        
        current_x = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))
        current_iteration += 1

    if current_iteration == max_iteration:
        print("На данном интервале ответ не существует")
    else:
        print("Найденный ответ: {}, значение функции: {}".format(current_x, equation(current_x)))