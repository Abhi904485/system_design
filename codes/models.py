from django.db import models
from problem.models import Problem
# Create your models here.


class Codes(models.Model):
    problem = models.ForeignKey(to=Problem, to_field='id', verbose_name="problem", related_name='Codes',
                                related_query_name='Code', on_delete=models.CASCADE, db_column='problem')
    name = models.CharField(name="name", max_length=500, verbose_name='name', db_column='name')
    java = models.TextField(name="java", max_length=5000, verbose_name='java', db_column='java')
    python = models.TextField(name="python", max_length=5000, verbose_name='python', db_column='python')

    class Meta:
        verbose_name = "Codes"
        verbose_name_plural = "Codes"
        db_table = 'codes'

    def __str__(self):
        return str(self.name)
