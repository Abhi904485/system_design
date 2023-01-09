from django.core.management.base import BaseCommand
from problem.models import Problem


class Command(BaseCommand):
    help = "Insert Problems"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Enter the problem name")
        parser.add_argument('description', type=str, help="Enter the problem description")

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        Problem.objects.create(name=name, description=description)
