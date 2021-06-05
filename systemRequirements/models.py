from django.db import models
from problem.models import Problem
# Create your models here.


class SystemRequirement(models.Model):
    """Model definition for SystemRequirements."""
    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='SystemRequirements',
                                related_query_name='SystemRequirement', on_delete=models.CASCADE, db_column='problem')
    requirement = models.TextField(name="requirement", verbose_name='requirement', max_length=5000, db_column='requirement')

    class Meta:
        """Meta definition for SystemRequirements."""

        verbose_name = 'SystemRequirements'
        verbose_name_plural = 'SystemRequirements'
        db_table = 'system_requirement'

    def __str__(self):
        """Unicode representation of SystemRequirements."""
        return "{}".format(str(self.requirement))
