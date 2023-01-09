from django.shortcuts import render
from problem.models import Problem
from django.core.paginator import Paginator


def home(request):
    problems = Problem.objects.all().order_by('pk')
    paginator = Paginator(problems, 4)
    page = request.GET.get('page')
    paged_problems = paginator.get_page(page)
    context = {
        'problems': paged_problems
    }
    return render(request, 'home.html', context=context)
