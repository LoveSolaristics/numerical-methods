from django.shortcuts import render
from chord_method.services import chord_method_solution
from django import forms


class TaskForm(forms.Form):
    equation = forms.CharField(label='Уравнение = 0')
    equation.widget.attrs['placeholder'] = 'x^3 - 2*x - 5'
    equation.widget.attrs['value'] = 'x^3 - 2*x - 5'

    error = forms.CharField(label='Погрешность')
    error.widget.attrs['placeholder'] = '0.001'
    error.widget.attrs['value'] = '0.001'

    a = forms.CharField(label='Левая граница')
    a.widget.attrs['placeholder'] = '2'
    a.widget.attrs['value'] = '2'

    b = forms.CharField(label='Правая граница')
    b.widget.attrs['placeholder'] = '3'
    b.widget.attrs['value'] = '3'


def index(request):
    solution_text = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            equation = form.cleaned_data['equation']
            e = float(form.cleaned_data['error'])
            a = float(form.cleaned_data['a'])
            b = float(form.cleaned_data['b'])

            try:
                solution = chord_method_solution(equation, e, a, b)
            except TypeError:
                solution = 'Вероятно вы неверно ввели параметры'
            except ValueError:
                solution = 'Функция на концах интервала принимает значения одного знака - условие ' \
                           'сходимости метода не выполнено '

            solution_text = 'Ответ: {}'.format(solution)

    else:
        form = TaskForm()

    return render(request, 'chord_method/index.html',
                  {'form': form, 'solution_text': solution_text})
