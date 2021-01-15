from django.shortcuts import render
from jacobi_method.services import jacobi_method_solution
from django import forms
import numpy as np



class TaskForm(forms.Form):
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



def index(request):
    solution_text = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
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

            solution_text = '| '
            for elem in solution:
                solution_text += str(elem) + ' | '
    else:
        form = TaskForm()

    return render(request, 'jacobi_method/index.html',
                  {'form': form, 'solution_text': solution_text})
