from typing import Callable
import derivative

def solve_equation(equation: Callable[[float], float], interval: list[float], accuracy: float):
    a: float = interval[0]
    b: float = interval[1]

    l: float = find_lambda(equation, a, b)

    phi: Callable[[float], float] = lambda x: x + equation(x) * l
    derivate_of_phi: Callable[[float], float] = lambda x: 1 + derivative.nth(equation, 1, x) * l

    q: float = find_q(derivate_of_phi, a, b)

    if q >= 1:
        print("q > 1, следовательно не выполняется достаточное условие сходимости и метод не сойдется к ответу")
        return None

    print("lambda = {}, q = {}".format(round(l, 5), round(q, 5)))
    print("phi(x) = x + f(x) * {}".format(round(l, 5)))

    if q > 0.5:
        check = lambda accuracy, xi, xi_prev, q: abs(xi - xi_prev) > accuracy
    else:
        check = lambda accuracy, xi, xi_prev, q: abs(xi - xi_prev) >= (1 - q / q) * accuracy

    x0: float = a
    x1: float = phi(x0)

    xi: float = x1
    xi_prev: float = x0

    iterations: int = 0

    while check(accuracy, xi, xi_prev, q):
        xi_prev = xi
        xi = phi(xi)
        iterations += 1

    answer_data: dict = {}
    answer_data['Ответ']: float = xi
    answer_data['Значение функции']: float = equation(xi)
    answer_data['Количество итераций']: float = iterations

    return answer_data


def find_lambda(equation: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(derivative.nth(equation, 1, start))
    while start < stop:
        if max_derivative < abs(derivative.nth(equation, 1, start)):
            max_derivative = abs(derivative.nth(equation, 1, start))
        start += 0.01
    return -1 / max_derivative


def find_q(equation: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(equation(start))
    while start < stop:
        if max_derivative < abs(equation(start)):
            max_derivative = abs(equation(start))
        start += 0.01
    return max_derivative


def solve_system_of_equations(system_of_equations: list[Callable[[float], float]], interval: list[float], accuracy: float):

    iterations = 0

    try:

        previous_x, previous_y = interval[0], interval[1]

        current_x = system_of_equations[0](previous_x, previous_y)
        current_y = system_of_equations[1](previous_x, previous_y)

        while abs(current_x - previous_x) > accuracy or abs(current_y - previous_y) > accuracy:

            previous_x, previous_y = current_x, current_y

            current_x = system_of_equations[0](previous_x, previous_y)
            current_y = system_of_equations[1](previous_x, previous_y)

            iterations += 1
    except OverflowError:
        print("Достаточное условие сходимости не выполняется")
        return None
            
    answer_data = {}
    answer_data['Ответ'] = [current_x, current_y]
    answer_data['Значение функции'] = [current_x - system_of_equations[0](previous_x, previous_y), current_y - system_of_equations[1](previous_x, previous_y)]
    answer_data['Вектор погрешностей'] = [abs(current_x - previous_x), abs(current_y - previous_y)]
    answer_data['Количество итераций'] = iterations

    return answer_data
        