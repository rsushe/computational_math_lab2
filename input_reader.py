from pathlib import Path
from math import sin, cos, asin

def read_user_choice(range, user_text):
    user_choice = -1
    while user_choice not in range:
        try:
            user_choice = int(input(user_text))
            break      
        except ValueError:
            continue
    return user_choice


def read_data():
    equation_type_choice = read_user_choice([1, 2], "Введите 1 чтобы выбрать одно уравнение, либо введите 2 чтобы выбрать систему уравнений: ")

    if equation_type_choice == 1:
        selected_equation, selected_equation_with_expressed_x = read_single_equation()
        method_choice = read_user_choice([1, 2, 3], "Введите 1 чтобы выбрать метод Хорд, 2 чтобы выбрать метод секущих или 3 чтобы выбрать метод простой итерации: ")
    else:
        selected_equation, selected_equation_with_expressed_x = read_system_of_equation()
        method_choice = 4
    

    input_stream_choice = read_user_choice([1, 2], "Введите 1 если исходные данные задаются через консоль, либо введите 2 если исходные данные задаются через файл: ")

    if input_stream_choice == 1:
        interval, accuracy = read_input_data_from_console()
    else:
        filename = input("Введите имя файла: ")
        while not Path(filename).is_file():
            filename = input("Файла по такому пути не существует, повторите ввод: ")

        interval, accuracy = read_input_data_from_file(filename=filename)

    return method_choice, selected_equation, selected_equation_with_expressed_x, interval, accuracy


def read_single_equation():
    print("1: -1.4x^3 - 0.9x^2 + 10.67x - 2.34")
    print("2: x^2 - 2x + 1")
    print("3: sin(x) - cos(x) + 1.5x")

    first_equation = lambda x: -1.4 * x ** 3 - 0.9 * x ** 2 + 10.67 * x - 2.34
    second_equation = lambda x: x ** 2 - 2 * x + 1
    third_equation = lambda x: sin(x) - cos(x) + 1.5 * x

    derivative_of_first_equation = lambda x: -4.2 * x ** 2 - 1.8 * x + 10.67
    derivative_of_second_equation = lambda x: 2 * x - 2
    derivative_of_third_equation = lambda x: cos(x) + sin(x) + 1.5

    equations = [(first_equation, derivative_of_first_equation), 
                (second_equation, derivative_of_second_equation), 
                (third_equation, derivative_of_third_equation)]

    user_choice = read_user_choice([1, 2, 3], "Введите номер желаемого выражения: ")

    return equations[user_choice - 1]


def read_system_of_equation():
    print("1: { -0.3 + 0.1x^2 + 0.2y^2 + x, -0.7 + 0.2x^2 + 0.1xy + y }")
    print("2: { sin(x) + y - 1, -2x^3 - 4y + 5")
    # -0.3+0.1x^2+0.2y^2+x=0, -0.7+0.2x^2+0.1xy+y=0
    first_equation = [lambda x, y : -0.3 + 0.1 * x ** 2 + 0.2 * y ** 2 + x, lambda x, y : -0.7 + 0.2 * x ** 2 + 0.1 * x * y + y]
    second_equation = [lambda x, y : sin(x) + y - 1, lambda x, y : -2 * x ** 3 - 4 * y + 5]

    first_equation_with_expressed_x = [lambda x, y : 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2, lambda x, y : 0.7 - 0.2 * x ** 2 + 0.1 * x * y]
    second_equation_with_expressed_x = [lambda x, y : asin(1 - y), lambda x, y : (5 - 2 * x ** 3) / -4]

    equations = [(first_equation, first_equation_with_expressed_x), (second_equation, second_equation_with_expressed_x)]

    user_choice = read_user_choice([1, 2], "Введите номер желаемого выражения: ")

    return equations[user_choice - 1]


def read_input_data_from_console():
    print("Введите начальную границу интервала: ", end="")
    while True:
        try:
            interval_start = float(input())
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue
    
    print("Введите конечную границу интервала: ", end="")
    while True:
        try:
            interval_end = float(input())
            if interval_end <= interval_start:
                print("Конец интервала должен быть строго больше чем начало интервала, повторите ввод: ", end="")
                continue
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue

    print("Введите желаемую точность: ", end="")
    while True:
        try:
            accuracy = float(input())
            if accuracy <= 0:
                print("Точность не может быть отрицательной, повторите ввод: ", end="")
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue

    return [interval_start, interval_end], accuracy

    

def read_input_data_from_file():
    pass