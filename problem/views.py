from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Problem
from systemRequirements.models import SystemRequirement
from useCaseDiagram.models import UseCaseDiagram, UseCases, Actors
from classDiagram.models import Class, ClassDiagram
from activityDiagram.models import ActivityDiagram
from codes.models import Codes
# Create your views here.


def problems(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    requirements = [requirement.requirement for requirement in problem.SystemRequirements.all()]
    use_case_diagram = get_object_or_404(UseCaseDiagram, problem=problem)
    actors = [actor.actor for actor in use_case_diagram.actors.all()]
    usecases = [usecase.use_case for usecase in use_case_diagram.usecases.all()]
    class_diagram = get_object_or_404(ClassDiagram, problem=problem)
    classes = [class_.name for class_ in class_diagram.Classes.all()]
    activity_diagrams = get_list_or_404(ActivityDiagram, problem=problem)
    codes = get_list_or_404(Codes, problem=problem)
    context = {
        'problem': problem,
        'requirements': requirements,
        'use_case_diagram': use_case_diagram,
        'actors': actors,
        'usecases': usecases,
        'class_diagram': class_diagram,
        'classes': classes,
        'activity_diagrams': activity_diagrams,
        'codes': codes
    }
    return render(request, 'problem.html', context=context)
