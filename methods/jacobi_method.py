import streamlit as st
import numpy as np
from numpy.linalg import norm


def jacobi_method_solution(A, b, epsilon=1e-10, x0=None):
    if len(A) != len(A[0]) or len(A) != len(b):
        return None
    k, xk = 0, x0
    if x0 is None: xk = b[:]
    rk = b - np.dot(A, xk)

    result = [xk]
    while norm(rk) > epsilon:
        xk = xk + rk / np.diag(A)
        k += 1
        rk = b - np.dot(A, xk)

        result.append(xk)
    return result


def print_solution(A, b, epsilon=1e-5):
    solution = jacobi_method_solution(A, b, epsilon)

    solution_text = ''
    for string in solution:
        solution_text += '| '
        for elem in string:
            solution_text += str(elem) + ' | '
        solution_text += '\n\n'
    solution_text += '\n\nОтвет: ' + str(solution[-1][0]) + ' , ' + str(
        solution[-1][1])

    st.info(solution_text)


def jacobi_method_visualization():
    st.markdown("""# Метод Якоби\n
Подробнее о реализации этого методы вы можете почитать 
[здесь](https://ru.wikipedia.org/wiki/Метод_Якоби).
        """)

    equation_count = st.selectbox('Количество уравнений в системе',
                                  [2, 3, 4])

    if equation_count == 2:
        col1, col2, col3 = st.columns(3)
        a11 = col1.number_input('Коэффициент матрицы A', key=11)
        a21 = col1.number_input('Коэффициент матрицы A', key=21)

        a12 = col2.number_input('Коэффициент матрицы A', key=12)
        a22 = col2.number_input('Коэффициент матрицы A', key=22)

        b1 = col3.number_input('Коэффициент матрицы b', key=1)
        b2 = col3.number_input('Коэффициент матрицы b', key=2)

        epsilon = col1.number_input('Погрешность', format='%.5f', value=0.01)

        if st.button('Решить систему'):
            A = np.array([[a11, a12], [a21, a22]])
            b = np.array([b1, b2])

            print_solution(A, b, epsilon)

    elif equation_count == 3:
        col1, col2, col3, col4 = st.columns(4)
        a11 = col1.number_input('Коэффициент матрицы A', key=11)
        a21 = col1.number_input('Коэффициент матрицы A', key=21)
        a31 = col1.number_input('Коэффициент матрицы A', key=31)

        a12 = col2.number_input('Коэффициент матрицы A', key=12)
        a22 = col2.number_input('Коэффициент матрицы A', key=22)
        a32 = col2.number_input('Коэффициент матрицы A', key=32)

        a13 = col3.number_input('Коэффициент матрицы A', key=13)
        a23 = col3.number_input('Коэффициент матрицы A', key=23)
        a33 = col3.number_input('Коэффициент матрицы A', key=33)

        b1 = col4.number_input('Коэффициент матрицы b', key=1)
        b2 = col4.number_input('Коэффициент матрицы b', key=2)
        b3 = col4.number_input('Коэффициент матрицы b', key=3)

        epsilon = col1.number_input('Погрешность', format='%.5f', value=0.01)

        if st.button('Решить систему'):
            A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
            b = np.array([b1, b2, b3])

            print_solution(A, b, epsilon)

    else:
        col1, col2, col3, col4, col5 = st.columns(5)
        a11 = col1.number_input('Коэффициент матрицы A', key=11)
        a21 = col1.number_input('Коэффициент матрицы A', key=21)
        a31 = col1.number_input('Коэффициент матрицы A', key=31)
        a41 = col1.number_input('Коэффициент матрицы A', key=41)

        a12 = col2.number_input('Коэффициент матрицы A', key=12)
        a22 = col2.number_input('Коэффициент матрицы A', key=22)
        a32 = col2.number_input('Коэффициент матрицы A', key=32)
        a42 = col2.number_input('Коэффициент матрицы A', key=42)

        a13 = col3.number_input('Коэффициент матрицы A', key=13)
        a23 = col3.number_input('Коэффициент матрицы A', key=23)
        a33 = col3.number_input('Коэффициент матрицы A', key=33)
        a43 = col3.number_input('Коэффициент матрицы A', key=43)

        a14 = col4.number_input('Коэффициент матрицы A', key=14)
        a24 = col4.number_input('Коэффициент матрицы A', key=24)
        a34 = col4.number_input('Коэффициент матрицы A', key=34)
        a44 = col4.number_input('Коэффициент матрицы A', key=44)

        b1 = col5.number_input('Коэффициент матрицы b', key=1)
        b2 = col5.number_input('Коэффициент матрицы b', key=2)
        b3 = col5.number_input('Коэффициент матрицы b', key=3)
        b4 = col5.number_input('Коэффициент матрицы b', key=4)

        epsilon = col1.number_input('Погрешность', format='%.5f', value=0.01)

        if st.button('Решить систему'):
            A = np.array([[a11, a12, a13, a14], [a21, a22, a23, a24],
                          [a31, a32, a33, a34],
                          [a41, a42, a43, a44]])
            b = np.array([b1, b2, b3, b4])

            print_solution(A, b, epsilon)
