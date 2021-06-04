from django.shortcuts import render
from problem.models import Problem


def home(request):
    problems = Problem.objects.all()
    context = {
        'problems': problems
    }
    return render(request, 'home.html', context=context)
