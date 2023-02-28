from pathlib import Path
from functions import single_equations, system_of_equations

def read_user_choice(range: list[int], user_text: str):
    user_choice: int = -1
    while user_choice not in range:
        try:
            user_choice: int = int(input(user_text))
            break      
        except ValueError:
            continue
    return user_choice


def read_data():
    equation_type_choice: int = read_user_choice([1, 2], "Введите 1 чтобы выбрать одно уравнение, либо введите 2 чтобы выбрать систему уравнений: ")

    if equation_type_choice == 1:
        selected_equation, selected_equation_with_expressed_x = read_single_equation()
        method_choice: int = read_user_choice([1, 2, 3], "Введите 1 чтобы выбрать метод Хорд, 2 чтобы выбрать метод секущих или 3 чтобы выбрать метод простой итерации: ")
    else:
        selected_equation, selected_equation_with_expressed_x = read_system_of_equation()
        method_choice: int = 4
    

    input_stream_choice: int = read_user_choice([1, 2], "Введите 1 если исходные данные задаются через консоль, либо введите 2 если исходные данные задаются через файл: ")

    if input_stream_choice == 1:
        interval, accuracy = read_input_data_from_console()
    else:
        filename: str = input("Введите имя файла: ")
        while not Path(filename).is_file():
            filename: str = input("Файла по такому пути не существует, повторите ввод: ")

        interval, accuracy = read_input_data_from_file(filename=filename)

    return method_choice, selected_equation, selected_equation_with_expressed_x, interval, accuracy


def read_single_equation():
    print("1: {}".format(single_equations.equations_string[0]))
    print("2: {}".format(single_equations.equations_string[1]))
    print("3: {}".format(single_equations.equations_string[2]))

    user_choice: int = read_user_choice([1, 2, 3], "Введите номер желаемого выражения: ")

    return single_equations.equations[user_choice - 1], single_equations.derivatives_of_equations[user_choice - 1]


def read_system_of_equation():
    print("1: {}".format(system_of_equations.system_of_equations[0]))
    print("2: {}".format(system_of_equations.system_of_equations[1]))

    user_choice: int = read_user_choice([1, 2], "Введите номер желаемого выражения: ")

    return system_of_equations.system_of_equations[user_choice - 1], system_of_equations.derivatives_of_system_of_equations[user_choice - 1]


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