from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Problem
from useCaseDiagram.models import UseCaseDiagram
from classDiagram.models import ClassDiagram
from activityDiagram.models import ActivityDiagram
from sequenceDiagram.models import SequenceDiagram
from codes.models import Codes
# Create your views here.


def problems(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    requirements = [requirement.requirement for requirement in problem.SystemRequirements.all()]
    use_case_diagram = get_object_or_404(UseCaseDiagram, problem=problem)
    actors = [actor for actor in use_case_diagram.actors.all()]
    usecases = [usecase for usecase in use_case_diagram.usecases.all()]
    class_diagram = get_object_or_404(ClassDiagram, problem=problem)
    classes = [class_ for class_ in class_diagram.Classes.all()]
    activity_diagrams = get_list_or_404(ActivityDiagram, problem=problem)
    sequence_diagrams = SequenceDiagram.objects.filter(problem=problem).all()
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
        'sequence_diagrams': sequence_diagrams,
        'codes': codes
    }
    if problem.name == 'Design a Movie Ticket Booking System':
        context.update({'concurrency': True})
    if problem.name == 'Design an ATM':
        context.update({'atm': True})
    if problem.name == 'Design Blackjack and a Deck of Cards':
        context.update({'jack': True})
    if problem.name == 'Design Facebook - a social network':
        context.update({'facebook': True})
    return render(request, 'problem.html', context=context)
