from typing import Callable

def solve_equation(equation: Callable[[float], float], interval: list[float], accuracy: float):
    a: float = interval[0]
    b: float = interval[1]

    if equation(a) * equation(b) > 0:
        print("На данном интервале ответ не существует")
        return None
    
    iterations: int = 0

    current_x: float = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))

    while abs(equation(current_x)) > accuracy:

        if equation(a) * equation(current_x) > 0:
            a = current_x
        else:
            b = current_x
        
        current_x = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))

        iterations += 1
    
    answer_data: dict = {}
    answer_data['Ответ']: float = current_x
    answer_data['Значение функции']: float = equation(current_x)
    answer_data['Количество итераций']: int = iterations

    return answer_data