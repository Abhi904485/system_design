from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Problem(models.Model):
    name = models.CharField(name='name', verbose_name="Problem Name", db_column="name", max_length=500)
    description = models.CharField(name='description', verbose_name="Problem Description", db_column="description", max_length=5000)
    image = models.ImageField(name='image', verbose_name='image', upload_to='problem')

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"
        db_table = "problem"

    def __str__(self):
        return "{}".format(self.name)
