import input_reader
from methods import chord_method, secant_method, simple_iteration_method


if __name__ == "__main__":
    try:

        method_choice, equation, derivative_of_equation, interval, accuracy = input_reader.read_data()
        print("a = {}, b = {}".format(interval[0], interval[1]))

        if method_choice == 1:
            chord_method.solve_equation(equation=equation, interval=interval, accuracy=accuracy)
        elif method_choice == 2:
            secant_method.solve_equation(equation=equation, interval=interval, accuracy=accuracy)
        elif method_choice == 3:
            simple_iteration_method.solve_equation(equation=equation, derivate_of_equation=derivative_of_equation, interval=interval, accuracy=accuracy)
        elif method_choice == 4:
            simple_iteration_method.solve_system_of_equations(system_of_equation_with_expressed_x=derivative_of_equation, interval=interval, accuracy=accuracy)

    except Exception as e:
        print(str(e))
        print("Программа завершена")
    except KeyboardInterrupt:
        print("Программа завершена из-за неправильного ввода")