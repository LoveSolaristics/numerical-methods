import numpy as np
from math import log, log10, e, tan, sin, cos
from decimal import Decimal, ROUND_05UP
import matplotlib.pyplot as plt


def figure_png(function, left_border, right_border):
    x = np.linspace(left_border, right_border, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, function(x), color='g', linewidth=2)
    fig.savefig('templates/dichotomy_plot.png')


def normalization_str(string):
    string = string.replace('tg', 'tan')
    string = string.replace('lg', 'log10')
    string = string.replace('ln', 'log')
    string = string.replace('^', '**')
    return string


def dichotomy_solution(f, error=10 ** (-3), method_error=1, left_border=-100, right_border=100,
                       details=False):
    function = lambda x: eval(normalization_str(f))
    figure_png(function, left_border, right_border)

    round_number = -int(log10(error))

    if function(left_border) * function(right_border) > 0:
        raise ValueError(
            'Функция на концах интервала принимает значения одного знака:\nf({}) = {} \nf({}) = {}'.format(
                left_border, function(left_border), right_border, function(right_border)))
    if not (method_error == 1 or method_error == 2):
        raise RuntimeError(
            f'Метод может быть либо первым (1), либо вторым (2). Вы передали в функцию '
            f'method_error = {method_error}')
    if function(left_border) == 0:
        return round(left_border, round_number)
    elif function(right_border) == 0:
        return round(right_border, round_number)

    if details:
        print('Сходимость метода к корню:\n', )
        print('{:-^55}'.format('-'))
        print('| {:^15} | {:^15} | {:^15} |'.format('Левая граница', 'Центр отрезка',
                                                    'Правая граница'))
        print('{:-^55}'.format('-'))

    while not ((method_error == 1 and abs(function((right_border + left_border) / 2)) < error) or (
            method_error == 2 and abs(left_border - right_border) < error)):

        middle = (right_border + left_border) / 2
        if details: print('| {:<15} | {:<15} | {:<15} |'.format(round(left_border, round_number),
                                                                round(middle, round_number),
                                                                round(right_border, round_number)))

        if function(middle) * function(left_border) < 0:
            right_border = middle
        elif function(middle) * function(right_border) < 0:
            left_border = middle
        else:
            raise ValueError(
                'Функция на концах интервала принимает значения одного знака:\nf({}) = {} \nf({}) = {}'.format(
                    left_border, function(left_border), right_border, function(right_border)))

    if details: print('{:-^55}'.format('-'))

    answer = Decimal((right_border + left_border) / 2)
    return float(answer.quantize(Decimal("1." + '0' * round_number)))
