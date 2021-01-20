from django.test import TestCase
from gradient_descent.services import *


class TestSolution(TestCase):
    number = 1

    @classmethod
    def setUpTestData(cls):
        print('\nТесты решающей функции метода градиентного спуска')
        pass

    def setUp(self):
        print('\n',self.number, ') Тест:', sep='', end=' ')
        TestSolution.number += 1
        pass

    def test_1(self):
        print("выражение из примера")
        f = ['x+x**2-2*y*z-0.1', 'y-y**2+3*x*z+0.2', 'z+z**2 + 2*x*y-0.3']
        func_answer = gradient_descent_solution(f, accuracy= 10 ** (-3), first_approach=[1, 1, 1])
        func_answer = [float(int(elem * 1000)) / 1000 for elem in func_answer]
        correct = [0.013, -0.177, 0.244]
        self.assertEqual(func_answer, correct)

    def test_2(self):
        print('переменные abc')
        f = ['a+a**2-2*b*c-0.1', 'b-b**2+3*a*c+0.2', 'c+c**2 + 2*a*b-0.3']
        func_answer = gradient_descent_solution(f, accuracy=10 ** (-3), first_approach=[1, 1, 1], variables='abc')
        func_answer = [float(int(elem * 1000)) / 1000 for elem in func_answer]
        correct = [0.013, -0.177, 0.244]
        self.assertEqual(func_answer, correct)


class TestNormalization(TestCase):
    number = 1

    @classmethod
    def setUpTestData(cls):
        print('\nТесты нормализации выражения')
        pass

    def setUp(self):
        print('\n',self.number, ') Тест:', sep='', end=' ')
        TestNormalization.number += 1
        pass

    def test_1(self):
        print("нет замен")
        f = ['x+x**2-2*y*z-0.1', 'y-y**2+3*x*z+0.2', 'z+z**2 + 2*x*y-0.3']
        self.assertEqual(f, normalization_str(f))

    def test_2(self):
        print("степени")
        f = normalization_str(['x+x^2-2*y*z-0.1', 'y-y^2+3*x*z+0.2', 'z+z^2 + 2*x*y-0.3'])
        correct = ['x+x**2-2*y*z-0.1', 'y-y**2+3*x*z+0.2', 'z+z**2 + 2*x*y-0.3']
        self.assertEqual(f, correct)
