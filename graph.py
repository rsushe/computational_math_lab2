import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from typing import Callable

def plot_function(equation: Callable[[float], float], root: float, start: float, stop: float):
    plt.figure(figsize=(8, 8))

    plt.axhline(y = 0, color = 'k', linestyle = '-')

    x = np.arange(start, stop, 0.01)
    plt.plot([i for i in x], [equation(i) for i in x])

    if root is not None:
        plt.plot(root, equation(root), marker='o', markerfacecolor="red")

    plt.title(f"Root in [{start},{stop}]")
    plt.grid(True)
    plt.show()


def plot_system(equation1: Callable[[float], float], equation2: Callable[[float], float]):
    x, y = sp.symbols("x y")
    sp.plot_implicit(sp.Or(sp.Eq(equation1(x, y), 0), sp.Eq(equation2(x, y), 0)))