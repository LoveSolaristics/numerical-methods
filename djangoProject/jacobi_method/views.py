from django.shortcuts import render
from jacobi_method.services import jacobi_method_solution
from django import forms
import numpy as np


class TaskForm3(forms.Form):
    index_a00 = forms.CharField(label='a00')
    index_a01 = forms.CharField(label='a01')
    index_a02 = forms.CharField(label='a02')
    index_a00.widget.attrs['placeholder'] = 'A 0 0'
    index_a01.widget.attrs['placeholder'] = 'A 0 1'
    index_a02.widget.attrs['placeholder'] = 'A 0 2'

    index_b0 = forms.CharField(label='b0')
    index_b0.widget.attrs['placeholder'] = 'B 0'

    index_a10 = forms.CharField(label='a10')
    index_a11 = forms.CharField(label='a11')
    index_a12 = forms.CharField(label='a12')
    index_a10.widget.attrs['placeholder'] = 'A 1 0'
    index_a11.widget.attrs['placeholder'] = 'A 1 1'
    index_a12.widget.attrs['placeholder'] = 'A 1 2'

    index_b1 = forms.CharField(label='b1')
    index_b1.widget.attrs['placeholder'] = 'B 1'

    index_a20 = forms.CharField(label='a20')
    index_a21 = forms.CharField(label='a21')
    index_a22 = forms.CharField(label='a22')
    index_a20.widget.attrs['placeholder'] = 'A 2 0'
    index_a21.widget.attrs['placeholder'] = 'A 2 1'
    index_a22.widget.attrs['placeholder'] = 'A 2 2'

    index_b2 = forms.CharField(label='b2')
    index_b2.widget.attrs['placeholder'] = 'B 2'

    epsilon = forms.CharField(label='epsilon')
    epsilon.widget.attrs['placeholder'] = 'ε'


class TaskForm4(forms.Form):
    index_a00 = forms.CharField(label='a00')
    index_a01 = forms.CharField(label='a01')
    index_a02 = forms.CharField(label='a02')
    index_a03 = forms.CharField(label='a03')
    index_a00.widget.attrs['placeholder'] = 'A 0 0'
    index_a01.widget.attrs['placeholder'] = 'A 0 1'
    index_a02.widget.attrs['placeholder'] = 'A 0 2'
    index_a03.widget.attrs['placeholder'] = 'A 0 3'

    index_b0 = forms.CharField(label='b0')
    index_b0.widget.attrs['placeholder'] = 'B 0'

    index_a10 = forms.CharField(label='a10')
    index_a11 = forms.CharField(label='a11')
    index_a12 = forms.CharField(label='a12')
    index_a13 = forms.CharField(label='a13')
    index_a10.widget.attrs['placeholder'] = 'A 1 0'
    index_a11.widget.attrs['placeholder'] = 'A 1 1'
    index_a12.widget.attrs['placeholder'] = 'A 1 2'
    index_a13.widget.attrs['placeholder'] = 'A 1 3'

    index_b1 = forms.CharField(label='b1')
    index_b1.widget.attrs['placeholder'] = 'B 1'

    index_a20 = forms.CharField(label='a20')
    index_a21 = forms.CharField(label='a21')
    index_a22 = forms.CharField(label='a22')
    index_a23 = forms.CharField(label='a23')
    index_a20.widget.attrs['placeholder'] = 'A 2 0'
    index_a21.widget.attrs['placeholder'] = 'A 2 1'
    index_a22.widget.attrs['placeholder'] = 'A 2 2'
    index_a23.widget.attrs['placeholder'] = 'A 2 3'

    index_b2 = forms.CharField(label='b2')
    index_b2.widget.attrs['placeholder'] = 'B 2'

    index_a30 = forms.CharField(label='a30')
    index_a31 = forms.CharField(label='a31')
    index_a32 = forms.CharField(label='a32')
    index_a33 = forms.CharField(label='a33')
    index_a30.widget.attrs['placeholder'] = 'A 3 0'
    index_a31.widget.attrs['placeholder'] = 'A 3 1'
    index_a32.widget.attrs['placeholder'] = 'A 3 2'
    index_a33.widget.attrs['placeholder'] = 'A 3 3'

    index_b3 = forms.CharField(label='b3')
    index_b3.widget.attrs['placeholder'] = 'B 3'

    epsilon = forms.CharField(label='epsilon')
    epsilon.widget.attrs['placeholder'] = 'ε'


class TaskForm2(forms.Form):
    index_a00 = forms.CharField(label='a00')
    index_a01 = forms.CharField(label='a01')
    index_a00.widget.attrs['placeholder'] = 'A 0 0'
    index_a01.widget.attrs['placeholder'] = 'A 0 1'

    index_b0 = forms.CharField(label='b0')
    index_b0.widget.attrs['placeholder'] = 'B 0'

    index_a10 = forms.CharField(label='a10')
    index_a11 = forms.CharField(label='a11')
    index_a10.widget.attrs['placeholder'] = 'A 1 0'
    index_a11.widget.attrs['placeholder'] = 'A 1 1'

    index_b1 = forms.CharField(label='b1')
    index_b1.widget.attrs['placeholder'] = 'B 1'

    epsilon = forms.CharField(label='epsilon')
    epsilon.widget.attrs['placeholder'] = 'ε'


def index(request):
    return render(request, 'jacobi_method/index.html', {})


def solve2(request):
    solution_text = ''
    if request.method == 'POST':
        form = TaskForm2(request.POST)
        if form.is_valid():
            A = [[0 for i in range(2)] for j in range(2)]
            for i in range(2):
                for j in range(2):
                    A[i][j] = float(form.cleaned_data['index_a' + str(i) + str(j)])
            A = np.array(A)

            b = [0, 0]
            for i in range(2):
                b[i] = float(form.cleaned_data['index_b' + str(i)])

            epsilon = float(form.cleaned_data['epsilon'])
            solution = jacobi_method_solution(A, b, epsilon)

            solution_text = ''
            for string in solution:
                solution_text += '| '
                for elem in string:
                    solution_text += str(elem) + ' | '
                solution_text += '<br />'
            solution_text += 'Ответ: ' + str(solution[-1][0]) + ' , ' + str(solution[-1][1])
    else:
        form = TaskForm2()

    return render(request, 'jacobi_method/2/index.html',
                  {'form': form, 'solution_text': solution_text})


def solve4(request):
    solution_text = ''
    if request.method == 'POST':
        form = TaskForm4(request.POST)
        if form.is_valid():
            A = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    A[i][j] = float(form.cleaned_data['index_a' + str(i) + str(j)])
            A = np.array(A)

            b = [0, 0, 0, 0]
            for i in range(4):
                b[i] = float(form.cleaned_data['index_b' + str(i)])

            epsilon = float(form.cleaned_data['epsilon'])
            solution = jacobi_method_solution(A, b, epsilon)

            solution_text = ''
            for string in solution:
                solution_text += '| '
                for elem in string:
                    solution_text += str(elem) + ' | '
                solution_text += '<br />'
            solution_text += 'Ответ: ' + str(solution[-1][0]) + ' , ' + str(
                solution[-1][1]) + ' , ' + str(solution[-1][2]) + ' , ' + str(solution[-1][3])
    else:
        form = TaskForm4()

    return render(request, 'jacobi_method/4/index.html',
                  {'form': form, 'solution_text': solution_text})


def solve3(request):
    solution_text = ''
    if request.method == 'POST':
        form = TaskForm3(request.POST)
        if form.is_valid():
            A = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    A[i][j] = float(form.cleaned_data['index_a' + str(i) + str(j)])
            A = np.array(A)

            b = [0, 0, 0]
            for i in range(3):
                b[i] = float(form.cleaned_data['index_b' + str(i)])

            epsilon = float(form.cleaned_data['epsilon'])
            solution = jacobi_method_solution(A, b, epsilon)

            solution_text = ''
            for string in solution:
                solution_text += '| '
                for elem in string:
                    solution_text += str(elem) + ' | '
                solution_text += '<br />'
            solution_text += 'Ответ: ' + str(solution[-1][0]) + ' , ' + str(
                solution[-1][1]) + ' , ' + str(solution[-1][2])
    else:
        form = TaskForm3()

    return render(request, 'jacobi_method/3/index.html',
                  {'form': form, 'solution_text': solution_text})
