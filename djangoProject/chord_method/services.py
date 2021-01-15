import numpy as np
from math import log, log10, e, tan, sin, cos
import matplotlib.pyplot as plt

def figure_png(function, left_border, right_border):
    x = np.linspace(left_border, right_border, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, function(x), color='g', linewidth=2)
    fig.savefig('templates/chord_method_plot.png')

def normalization_str(string):
    string = string.replace('tg', 'tan')
    string = string.replace('lg', 'log10')
    string = string.replace('^', '**')
    return string


def chord_method_solution(f, error=10 ** (-3), left_border=-10, right_border=10):
    function = lambda x: eval(normalization_str(f))
    figure_png(function, left_border, right_border)

    round_number = -int(log10(error))

    if function(left_border) * function(right_border) > 0:
        raise ValueError(
            'Функция на концах интервала принимает значения одного знака:\nf({}) = {} \nf({}) = {}'.format(
                left_border, function(left_border), right_border, function(right_border)))

    x_0 = left_border
    x_1 = right_border

    x_2 = x_1 - (function(x_1) * (x_1 - x_0)) / (function(x_1) - function(x_0))
    while abs(function(x_2)) > error:
        x_1 = x_2
        x_2 = x_1 - (function(x_1) * (x_1 - x_0)) / (function(x_1) - function(x_0))
    return round(x_2, round_number)
