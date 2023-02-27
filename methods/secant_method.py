def solve_equation(equation, interval, accuracy):
    previous_x = interval[0]
    current_x = previous_x + 0.03

    next_x = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))

    while abs(next_x - current_x) > accuracy:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - equation(current_x) * (current_x - previous_x) / (equation(current_x) - equation(previous_x))

    print("Найденный ответ: {}, значение функции: {}".format(current_x, equation(current_x)))
