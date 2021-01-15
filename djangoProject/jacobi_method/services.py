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
