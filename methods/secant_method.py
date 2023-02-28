from typing import Callable

def solve_equation(equation: Callable[[float], float], interval: list[float], accuracy: float):
    previous_x: float = interval[0]
    current_x: float = previous_x + 0.03

    next_x: float = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))

    current_iteration: int = 1
    max_iteration: int = 100000

    while abs(next_x - current_x) > accuracy and current_iteration < max_iteration:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))

        current_iteration += 1

    if current_iteration == max_iteration:
        print("На данном интервале ответ не существует")
    else:
        print("Найденный ответ: {}, значение функции: {}".format(current_x, equation(current_x)))
