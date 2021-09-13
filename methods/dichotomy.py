import streamlit as st
import numpy as np
from math import log, log10, e, tan, sin, cos
from decimal import Decimal, ROUND_05UP
import matplotlib.pyplot as plt


def normalization_str(string):
    string = string.replace('tg', 'tan')
    string = string.replace('lg', 'log10')
    string = string.replace('ln', 'log')
    string = string.replace('^', '**')
    return string


def dichotomy_solution(f, error=10 ** (-3), method_error=1, left_border=-100,
                       right_border=100,
                       details=False):
    f = normalization_str(f)
    function = lambda x: eval(f)

    round_number = -int(log10(error))

    if function(left_border) * function(right_border) > 0:
        raise ValueError(
            'Функция на концах интервала принимает значения одного знака:\nf({}) = {} \nf({}) = {}'.format(
                left_border, function(left_border), right_border,
                function(right_border)))
    if not (method_error == 1 or method_error == 2):
        raise RuntimeError(
            f'Метод может быть либо первым (1), либо вторым (2). Вы передали в функцию '
            f'method_error = {method_error}')
    if function(left_border) == 0:
        return round(left_border, round_number)
    elif function(right_border) == 0:
        return round(right_border, round_number)

    if details:
        st.text('Сходимость метода к корню:\n', )
        st.text('{:-^55}'.format('-'))
        st.text('| {:^15} | {:^15} | {:^15} |'.format('Левая граница',
                                                      'Центр отрезка',
                                                      'Правая граница'))
        st.text('{:-^55}'.format('-'))

    while not ((method_error == 1 and abs(
            function((right_border + left_border) / 2)) < error) or (
                       method_error == 2 and abs(
                   left_border - right_border) < error)):

        middle = (right_border + left_border) / 2
        if details:
            st.text('| {:<15} | {:<15} | {:<15} |'.format(
                round(left_border, round_number),
                round(middle, round_number),
                round(right_border, round_number)))

        if function(middle) * function(left_border) < 0:
            right_border = middle
        elif function(middle) * function(right_border) < 0:
            left_border = middle
        else:
            raise ValueError(
                'Функция на концах интервала принимает значения одного знака:\n\nf({}) = {} \n\nf({}) = {}'.format(
                    left_border, function(left_border), right_border,
                    function(right_border)))

    if details:
        st.text('{:-^55}'.format('-'))

    answer = Decimal((right_border + left_border) / 2)
    return float(answer.quantize(Decimal("1." + '0' * round_number)))


def dichotomy_visualization():
    st.markdown("""# Метод дихотомии\n
Подробнее о реализации этого методы вы можете почитать 
[здесь](http://www.machinelearning.ru/wiki/index.php?title=Методы_дихотомии).
    """)

    equation = st.text_input('Уравнение', help='Пример: x^3-18*x-83')
    st.info(
        'Необходимо вписать лишь одну часть уравнения, другая будет считаться 0')

    col1, col2 = st.columns(2)
    left_border = col1.number_input('Введите левую границу', value=-10.)
    right_border = col2.number_input('Введите правую границу', value=10.)

    epsilon = col1.number_input('Введите погрешность', min_value=1e-5,
                                max_value=1., value=0.001,
                                format='%.5f')

    method = col2.selectbox('Выберите метод вычисления погрешности',
                            ['по длине интервала', 'по значению функции'])

    method_code = 1 if method == 'по длине интервала' else 2

    if st.button('Решить уравнение') and equation:
        try:
            st.info(
                f'Ответ: {dichotomy_solution(equation, epsilon, method_code, left_border, right_border, True)}')
        except ValueError as value_error:
            st.warning(f"""{value_error}""")
        except SyntaxError as syntax_error:
            st.warning('Вероятно вы ввели уравнение неверно')
