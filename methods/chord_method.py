import numpy as np
from math import log, log10, e, tan, sin, cos
import plotly.express as px
import streamlit as st


def figure_png(function, left_border, right_border):
    x = np.linspace(left_border, right_border, 1000)
    fig = px.line(x=x, y=function(x), title='График уравнения')
    st.plotly_chart(fig)


def normalization_str(string):
    string = string.replace('tg', 'tan')
    string = string.replace('lg', 'log10')
    string = string.replace('^', '**')
    return string


def chord_method_solution(f, error=1e-3, left_border=-10, right_border=10):
    def function(x):
        return eval(normalization_str(f))

    figure_png(function, left_border, right_border)

    round_number = -int(log10(error))

    if function(left_border) * function(right_border) > 0:
        raise ValueError(
            'Функция на концах интервала принимает '
            'значения одного знака:\n\nf({}) = {} \n\nf({}) = {}'
                .format(left_border, function(left_border), right_border,
                        function(right_border)))

    x_0 = left_border
    x_1 = right_border

    x_2 = x_1 - (function(x_1) * (x_1 - x_0)) / (function(x_1) - function(x_0))
    while abs(function(x_2)) > error:
        x_1 = x_2
        x_2 = x_1 - (function(x_1) * (x_1 - x_0)) / (
                function(x_1) - function(x_0))
    return round(x_2, round_number)


def chord_method_visualization():
    st.markdown("""# Метод хорд\n
Подробнее о реализации этого методы вы можете почитать
 [здесь](https://ru.wikipedia.org/wiki/Метод_хорд).
    """)

    equation = st.text_input('Уравнение', help='Пример: x^3-18*x-83')
    st.info(
        'Необходимо вписать лишь одну часть уравнения,'
        ' другая будет считаться равной нулю')

    col1, col2 = st.columns(2)
    lb = col1.number_input('Введите левую границу', value=-10.)
    rb = col2.number_input('Введите правую границу', value=10.)

    epsilon = st.number_input('Введите погрешность', min_value=1e-5,
                              max_value=1., value=0.001,
                              format='%.5f')

    if st.button('Решить уравнение') and equation:
        try:
            st.info(
                f'Ответ: {chord_method_solution(equation, epsilon, lb, rb)}')
        except ValueError as value_error:
            st.warning(f"""{value_error}""")
        except SyntaxError as syntax_error:
            st.warning('Вероятно вы ввели уравнение неверно')
