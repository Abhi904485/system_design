from SystemDesign.utility import SVGAndImageField
from django.utils.safestring import mark_safe
from django.db import models
from problem.models import Problem
# Create your models here.


class ActivityDiagram(models.Model):
    """Model definition for ActivityDiagram."""

    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='ActivityDiagrams',
                                related_query_name='ActivityDiagram', on_delete=models.CASCADE, db_column='problem')
    activity = models.TextField(name="activity", verbose_name='activity', max_length=5000, db_column='activity')
    image = SVGAndImageField(name='image', verbose_name='image', upload_to='activityDiagram')

    class Meta:
        """Meta definition for ActivityDiagram."""

        verbose_name = 'ActivityDiagram'
        verbose_name_plural = 'ActivityDiagrams'
        db_table = 'activity'

    def custom_image_field(self):
        return mark_safe('<img src="{}" width=50 height=50/>'.format(self.image.url))
    
    custom_image_field.short_description = 'Image'
    custom_image_field.allow_tags = True

    def __str__(self):
        """Unicode representation of ActivityDiagram."""
        return str(self.activity)
