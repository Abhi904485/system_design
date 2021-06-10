from django.db import models
from django.utils.safestring import mark_safe
from SystemDesign.utility import SVGAndImageField
from problem.models import Problem
# Create your models here.


class SequenceDiagram(models.Model):
    """Model definition for SequenceDiagram."""
    
    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='SequenceDiagram',
                                related_query_name='SequenceDiagram', on_delete=models.CASCADE, db_column='problem')
    
    description = models.TextField(name="description", verbose_name="description", db_column='name', max_length=500)
    image =  SVGAndImageField(name='image', verbose_name='image', upload_to='sequenceDiagram')

    class Meta:
        """Meta definition for SequenceDiagram."""

        verbose_name = 'SequenceDiagram'
        verbose_name_plural = 'SequenceDiagrams'
        db_table = 'sequence_diagram'

    def custom_image_field(self):
        return mark_safe('<img src="{}" width=50 height=50/>'.format(self.image.url))
    
    custom_image_field.short_description = 'Image'
    custom_image_field.allow_tags = True

    def __str__(self):
        """Unicode representation of SequenceDiagram."""
        return str(self.description)
