from pathlib import Path
from functions import equation, system_of_equations

def read_user_choice(range: list[int], user_text: str):
    user_choice: int = -1
    while user_choice not in range:
        try:
            user_choice: int = int(input(user_text))      
        except ValueError:
            continue
    return user_choice


def read_data():
    data: dict = {}

    equation_type_choice: int = read_user_choice([1, 2], "Введите 1 чтобы выбрать одно уравнение, либо введите 2 чтобы выбрать систему уравнений: ")

    if equation_type_choice == 1:
        data['equation']: equation.Equation = read_single_equation()
        data['method']: int = read_user_choice([1, 2, 3], "Введите 1 чтобы выбрать метод Хорд, 2 чтобы выбрать метод секущих или 3 чтобы выбрать метод простой итерации: ")
    else:
        data['equation']: system_of_equations.SystemOfEquations = read_system_of_equation()
        

    input_stream_choice: int = read_user_choice([1, 2], "Введите 1 если исходные данные задаются через консоль, либо введите 2 если исходные данные задаются через файл: ")

    if input_stream_choice == 1:
        data['interval'], data['accuracy'] = read_input_data_from_console()
    else:
        filename: str = input("Введите имя файла: ")
        while not Path(filename).is_file():
            filename = input("Файла по такому пути не существует, повторите ввод: ")

        data['interval'], data['accuracy'] = read_input_data_from_file(filename=filename)

    return data


def read_single_equation():
    for i in range(len(equation.equations)):
        print("{}: {}".format(i + 1, equation.equations[i].string_representation))
    
    user_choice: int = read_user_choice([1, 2, 3], "Введите номер желаемого выражения: ")

    return equation.equations[user_choice - 1]


def read_system_of_equation():
    for i in range(len(system_of_equations.equations)):
        print("{}: {}".format(i + 1, system_of_equations.equations[i].string_representation))

    user_choice: int = read_user_choice([1, 2], "Введите номер желаемого выражения: ")

    return system_of_equations.equations[user_choice - 1]


def read_input_data_from_console():
    print("Введите начальную границу интервала: ", end="")
    while True:
        try:
            interval_start: float = float(input())
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue
    
    print("Введите конечную границу интервала: ", end="")
    while True:
        try:
            interval_end: float = float(input())
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
            accuracy: float = float(input())
            if accuracy <= 0:
                print("Точность не может быть отрицательной, повторите ввод: ", end="")
            break
        except ValueError:
            print("Неверный ввод, повторите попытку: ", end="")
            continue

    return [interval_start, interval_end], accuracy


def read_input_data_from_file(filename: str):
    with open(filename, 'r') as file:
        line: str = file.readline()
        
        try:
            data: list[float] = list(map(float, line.split(" ")))
        except ValueError:
            raise ValueError("Неверный тип данных в файле")
    
    if len(data) != 3:
        raise ValueError("В файле должно быть ровно 3 числа")

    if data[1] <= data[0]:
        raise ValueError("Конец интервала должен быть строго больше чем начало интервала")

    if data[2] <= 0:
        raise ValueError("Точность должна быть положительным числом")

    return [data[0], data[1]], data[2]
    