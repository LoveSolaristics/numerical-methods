import numpy as np
from math import log, log10, e, tan, sin, cos
from sympy import *


def deviation(F):
    result = 0
    for elem in F:
        result += abs(elem)
    return result


def nice_result(X, accuracy):
    X = [float(int(float(elem) * (1 / accuracy))) * accuracy for elem in X]
    return X


def print_vector(vector, accuracy=3):
    print(end='[')
    if accuracy == 2:
        for elem in vector:
            print('{:^.2f}'.format(elem), end=' ')
    elif accuracy == 3:
        for elem in vector:
            print('{:^.3f}'.format(elem), end=' ')
    else:
        for elem in vector:
            print('{:^.10f}'.format(elem), end=' ')
    print(']')


# заменяет вхождения
def normalization_str(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].replace('tg', 'tan')

        strings[i] = strings[i].replace('lg', 'log10')

        strings[i] = strings[i].replace('^', '**')
    return strings


def gradient_descent_solution(f, variables='xyz', first_approach=None, accuracy=10 ** (-3)):
    f = normalization_str(f)

    equations_count = len(f)
    x, y, z, a, b, c = symbols('x y z a b c')

    variables_count = len(variables)

    W = [[0 for j in range(variables_count)] for i in range(equations_count)]

    for i in range(equations_count):
        for j in range(variables_count):
            W[i][j] = diff(eval(f[i]), eval(variables[j]))

    X = [0 for i in range(variables_count)]

    symbols_dict = {variables[0]: X[0], variables[1]: X[1], variables[2]: X[2]}
    f_i = np.array([eval(f[i], symbols_dict) for i in range(equations_count)])

    while True:
        symbols_dict = {variables[0]: X[0], variables[1]: X[1], variables[2]: X[2]}
        f_i = np.array([eval(f[i], symbols_dict) for i in range(equations_count)])

        if accuracy >= deviation(f_i):
            break

        w_i = np.array([[eval(str(W[i][j]), symbols_dict) for j in range(variables_count)] for i in
                        range(equations_count)])

        wf = np.dot(w_i.transpose(), f_i)
        wwf = np.dot(w_i, wf)

        if np.dot(wwf, wwf) == 0:
            print('devision by zero')
            break

        mu = np.dot(f_i, wwf) / np.dot(wwf, wwf)

        deltaX = mu * np.dot(w_i.transpose(), f_i)
        X = X - deltaX

    # print_vector(X, -np.log10(accuracy))

    return nice_result(X, accuracy)
