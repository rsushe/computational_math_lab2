from typing import Callable
import derivative

def solve_equation(equation: Callable[[float], float], interval: list[float], accuracy: float):
    a: float = interval[0]
    b: float = interval[1]

    if equation(a) * equation(b) > 0:
        print("На данном интервале ответ не существует")
        return None
    
    if equation(a) * derivative.nth(equation, 2, a) > 0:
        previous_x: float = a
    else:
        previous_x: float = b

    current_x: float = previous_x + 0.03

    next_x: float = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))

    iterations: int = 0

    while abs(next_x - current_x) > accuracy:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))
        iterations += 1

    answer_data: dict = {}
    answer_data['Ответ']: float = current_x
    answer_data['Значение функции']: float = equation(current_x)
    answer_data['Количество итераций']: int = iterations

    return answer_data
