from django.shortcuts import render
from gradient_descent.services import gradient_descent_solution
from django import forms


class TaskForm(forms.Form):
    equation_1 = forms.CharField(label='1')
    equation_2 = forms.CharField(label='2')
    equation_3 = forms.CharField(label='3')
    variables = forms.CharField(label='Переменные')


def index(request):
    solution_text = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            equations = [form.cleaned_data['equation_1'], form.cleaned_data['equation_2'],
                         form.cleaned_data['equation_3']]
            solution = gradient_descent_solution(
                equations, variables=form.cleaned_data['variables'])

            solution_text = '{} = {:.3f}    {} = {:.3f}    {} = {:.3f}'.format(
                form.cleaned_data['variables'][0], solution[0], form.cleaned_data['variables'][1],
                solution[1], form.cleaned_data['variables'][2], solution[2])

    else:
        form = TaskForm()

    return render(request, 'gradient_descent/index.html',
                  {'form': form, 'solution_text': solution_text})
