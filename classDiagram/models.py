from django.db import models
from problem.models import Problem
from django.core.exceptions import ValidationError
# Create your models here.


class ClassDiagram(models.Model):
    """Model definition for ClassDiagram."""

    def validate_uml(self):
        if self.name.endswith(".svg") or self.name.endswith('.png'):
            pass
        else:
            raise ValidationError("File is not supported")

    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='ClassDiagrams',
                                related_query_name='ClassDiagram', on_delete=models.CASCADE, db_column='problem')
    image = models.ImageField(name='image', verbose_name='image', upload_to='classDiagram')
    uml = models.FileField(name='uml', verbose_name='uml', upload_to='uml', validators=[validate_uml])

    class Meta:
        """Meta definition for ClassDiagram."""

        verbose_name = 'ClassDiagram'
        verbose_name_plural = 'ClassDiagrams'
        db_table = "classdiagram"

    def __str__(self):
        """Unicode representation of ClassDiagram."""
        return str(self.problem.name + " class Diagram")


class Class(models.Model):
    """Model definition for Classes."""

    class_diagram = models.ForeignKey(to=ClassDiagram, to_field='id', verbose_name="class Diagram", related_name='Classes',
                                      related_query_name='Class', on_delete=models.CASCADE, db_column='Class')
    name = models.CharField(name='name', verbose_name='name', max_length=5000, db_column='name')

    class Meta:
        """Meta definition for Classes."""

        verbose_name = 'Class'
        verbose_name_plural = 'Class'
        db_table = 'class'

    def __str__(self):
        """Unicode representation of Classes."""
        return str(self.name)