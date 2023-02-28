from typing import Callable

def solve_equation(equation: Callable[[float], float], derivate_of_equation: Callable[[float], float], interval: list[float], accuracy: float):
    a: float = interval[0]
    b: float = interval[1]

    l: float = find_lambda(derivate_of_equation, a, b)

    phi: Callable[[float], float] = lambda x: x + equation(x) * l
    derivate_of_phi: Callable[[float], float] = lambda x: 1 + derivate_of_equation(x) * x

    q: float = find_q(derivate_of_phi, a, b)

    if q >= 1:
        print("q > 1, следовательно не выполняется достаточное условие сходимости метода, следовательно метод не сойдется к ответу")
        return

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

    while check(accuracy, xi, xi_prev, q):
        xi_prev = xi
        xi = phi(xi)

    print("Найденный ответ: {}, значение функции: {}".format(xi, equation(xi)))


def find_lambda(derivate_of_equation: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(derivate_of_equation(start))
    while start < stop:
        if max_derivative < abs(derivate_of_equation(start)):
            max_derivative = abs(derivate_of_equation(start))
        start += 0.01
    return -1 / max_derivative


def find_q(equation: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(equation(start))
    while start < stop:
        if max_derivative < abs(equation(start)):
            max_derivative = abs(equation(start))
        start += 0.01
    return max_derivative

def solve_system_of_equations(system_of_equation_with_expressed_x, interval, accuracy):
    current_iteration = 1
    max_iteration = 100000

    previous_x, previous_y = interval[0], interval[1]
    current_x = round(system_of_equation_with_expressed_x[0](previous_x, previous_y), 3)
    current_y = round(system_of_equation_with_expressed_x[1](previous_x, previous_y), 3)

    while (abs(current_x - previous_x) > accuracy or abs(current_y - previous_y) > accuracy) and current_iteration < max_iteration:

        previous_x, previous_y = current_x, current_y
        current_x = round(system_of_equation_with_expressed_x[0](previous_x, previous_y), 3)
        current_y = round(system_of_equation_with_expressed_x[1](previous_x, previous_y), 3)
        
        current_iteration += 1
    
    if current_iteration == max_iteration:
        print("На данном интервале ответ не существует")
    else:
        print("Найденный ответ: x = {}, y = {}".format(current_x, current_y))
        print("Значение первой функции: {}".format(system_of_equation_with_expressed_x[0](current_x, current_y)))
        print("Значение второй функции: {}".format(system_of_equation_with_expressed_x[1](current_x, current_y)))
        