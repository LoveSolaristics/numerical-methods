from django.test import TestCase
from dichotomy.services import *


class TestSolution(TestCase):
    number = 1

    @classmethod
    def setUpTestData(cls):
        print('\nТесты для решающей функции метода дихотомии')
        pass

    def setUp(self):
        print('\n', self.number, ') Тест:', sep='', end=' ')
        TestSolution.number += 1
        pass

    def test_1(self):
        print('квадратичная функция')
        f = 'x^2 - 4*x + 3'
        func_answer = dichotomy_solution(f, 0.001, 1, -0.5, 1.6, False)
        correct = 1
        self.assertEqual(func_answer, correct)

    def test_2(self):
        print("кубическая функция")
        f = 'x^3 - 2*x - 5'
        func_answer = dichotomy_solution(f, 0.001, 1, 2, 3, False)
        correct = 2.094
        self.assertEqual(func_answer, correct)

    def test_3(self):
        print("функция с косинусом")
        f = '10*cos(x) + 2'
        func_answer = dichotomy_solution(f, 10 ** (-5), 1, -0.5, 3, False)
        correct = 1.77215
        self.assertEqual(func_answer, correct)

    def test_4(self):
        print("функция с синусом")
        f = '10*sin(x) + 2'
        func_answer = dichotomy_solution(f, 10 ** (-3), 1, -1, 1)
        correct = -0.201
        self.assertEqual(func_answer, correct)

    def test_6(self):
        print("функция с тангенсом")
        f = '(tg(x)-1)^2-1'
        func_answer = dichotomy_solution(f, 10 ** (-3), 1, 0.5, 1.4)
        correct = 1.107
        self.assertEqual(func_answer, correct)

    def test_7(self):
        print("функция с натуральным логарифмом")
        f = 'ln(x)+1'
        func_answer = dichotomy_solution(f, 10 ** (-4), 1, 0.01, 1)
        correct = 0.3679
        self.assertEqual(func_answer, correct)

    def test_8(self):
        print("функция с десятичным логарифмом")
        f = 'lg(x)+1'
        func_answer = dichotomy_solution(f, 10 ** (-3), 1, 0.01, 1)
        correct = 0.100
        self.assertEqual(func_answer, correct)
