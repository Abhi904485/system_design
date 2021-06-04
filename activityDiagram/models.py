from django.db import models
from problem.models import Problem
from django.core.exceptions import ValidationError
# Create your models here.


class ActivityDiagram(models.Model):
    """Model definition for ActivityDiagram."""
    def validate_image(self):
        if self.name.endswith(".svg") or self.name.endswith('.png'):
            pass
        else:
            raise ValidationError("File is not supported")

    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='ActivityDiagrams',
                                related_query_name='ActivityDiagram', on_delete=models.CASCADE, db_column='problem')
    activity = models.CharField(name="activity", verbose_name='activity', max_length=5000, db_column='activity')
    image = models.FileField(name='image', verbose_name='image', upload_to='activityDiagram', validators=[validate_image])

    class Meta:
        """Meta definition for ActivityDiagram."""

        verbose_name = 'ActivityDiagram'
        verbose_name_plural = 'ActivityDiagrams'
        db_table = 'activity'

    def __str__(self):
        """Unicode representation of ActivityDiagram."""
        return str(self.activity)
