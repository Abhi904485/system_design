from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from SystemDesign.utility import SVGAndImageField
from django.db import models
from problem.models import Problem
# Create your models here.


class UseCaseDiagram(models.Model):
    """Model definition for UseCaseDiagram."""

    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='UseCaseDiagrams',
                                related_query_name='UseCaseDiagram', on_delete=models.CASCADE, db_column='problem')
    image = SVGAndImageField(name='image', verbose_name='image', upload_to='usecases')
    class Meta:
        """Meta definition for UseCaseDiagram."""

        verbose_name = 'UseCaseDiagram'
        verbose_name_plural = 'UseCaseDiagrams'
        db_table = 'usecasediagram'

    def custom_image_field(self):
        return mark_safe('<img src="{}" width=50 height=50/>'.format(self.image.url))
    
    custom_image_field.short_description = 'Image'
    custom_image_field.allow_tags = True

    def __str__(self):
        """Unicode representation of UseCaseDiagram."""
        return self.problem.name +" Usecase"


class Actors(models.Model):
    """Model definition for Actors."""

    usecasediagram = models.ForeignKey(to=UseCaseDiagram, to_field='id', verbose_name="usecasediagram", related_name="actors",
                                         related_query_name="actor", on_delete=models.CASCADE, db_column='usecasediagram')
    actor =  models.TextField(name="actor", verbose_name="actor",max_length=5000, db_column="actor")
    class Meta:
        """Meta definition for Actors."""

        verbose_name = 'Actors'
        verbose_name_plural = 'Actors'
        db_table = 'actor'

    def custom_actor(self):
        return truncatechars(self.actor, 150)
    
    custom_actor.short_description = "Actor"

    def __str__(self):
        """Unicode representation of Actors."""
        return self.actor +" Actor"


class UseCases(models.Model):
    """Model definition for UseCases."""
    usecasediagram = models.ForeignKey(to=UseCaseDiagram, to_field='id', verbose_name="usecases", related_name="usecases",
                                         related_query_name="usecase", on_delete=models.CASCADE, db_column='usecasediagram')
    use_case =  models.TextField(name="use_case", verbose_name="use_case",max_length=5000, db_column="use_case")

    class Meta:
        """Meta definition for UseCases."""

        verbose_name = 'UseCases'
        verbose_name_plural = 'UseCases'
        db_table = 'use_case'
    
    def custom_usecase(self):
        return truncatechars(self.use_case, 150)
    
    custom_usecase.short_description = "Usecase"

    def __str__(self):
        """Unicode representation of UseCases."""
        return self.use_case +" Use Case    "
