from django.shortcuts import render
from dichotomy.services import dichotomy_solution
from django import forms


class TaskForm(forms.Form):
    equation = forms.CharField(label='Уравнение = 0')
    equation.widget.attrs['placeholder'] = 'x^2 - 4*x + 3'
    equation.widget.attrs['value'] = 'x^2 - 4*x + 3'

    error = forms.CharField(label='Погрешность')
    error.widget.attrs['placeholder'] = '0.001'
    error.widget.attrs['value'] = '0.001'

    a = forms.CharField(label='Левая граница')
    a.widget.attrs['placeholder'] = '-0.5'
    a.widget.attrs['value'] = '-0.5'

    b = forms.CharField(label='Правая граница')
    b.widget.attrs['placeholder'] = '1.6'
    b.widget.attrs['value'] = '1.6'

    method = forms.ChoiceField(label='Метод вычисления погрешности',
                               choices=(('method_1', 'по длине интервала'),
                                        ('method_2', 'по значению функции')))


def index(request):
    solution_text = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            equation = form.cleaned_data['equation']
            e = float(form.cleaned_data['error'])
            a = float(form.cleaned_data['a'])
            b = float(form.cleaned_data['b'])
            m = 1 if form.cleaned_data['method'] == 'по длине интервала' else 2

            try:
                solution = dichotomy_solution(equation, e, m, a, b)
            except TypeError:
                solution = 'Вероятно вы неверно ввели параметры'
            except ValueError:
                solution = 'Функция на концах интервала принимает значения одного знака - условие ' \
                           'сходимости метода не выполнено '

            solution_text = 'Ответ: {}'.format(solution)

    else:
        form = TaskForm()

    return render(request, 'dichotomy/index.html',
                  {'form': form, 'solution_text': solution_text})
