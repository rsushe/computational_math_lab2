from data_io import data_reader, data_writer
from functions.system_of_equations import SystemOfEquations 
from methods import chord_method, secant_method, simple_iteration_method
from typing import Callable
import graph

if __name__ == "__main__":
    try:

        data: dict = data_reader.read_data()

        interval: list[float] = data['interval']
        equation: Callable[[float], float] = data['equation']
        accuracy: float = data['accuracy']

        if isinstance(equation, SystemOfEquations):

            answer_data: dict = simple_iteration_method.solve_system_of_equations(system_of_equations=equation.itself_with_expessed_x, interval=interval, accuracy=accuracy)
            
            if answer_data != None:
                data_writer.write_data(answer_data)
            
            graph.plot_system(equation.itself[0], equation.itself[1])
        else:

            equation: Callable[[float], float] = equation.itself

            method: int = data['method']

            answer_data: dict = None

            if method == 1:
                answer_data = chord_method.solve_equation(equation=equation, interval=interval, accuracy=accuracy)
            elif method == 2:
                answer_data = secant_method.solve_equation(equation=equation, interval=interval, accuracy=accuracy)
            elif method == 3:
                answer_data = simple_iteration_method.solve_equation(equation=equation, interval=interval, accuracy=accuracy)

            if answer_data != None:
                data_writer.write_data(answer_data)
            
            graph.plot_function(equation, answer_data['Ответ'], -5, 5)

    except Exception as e:
        print(str(e))
        print("Программа завершена")
    except KeyboardInterrupt:
        print("Программа завершена из-за неправильного ввода")