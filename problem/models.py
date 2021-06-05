from django.utils.safestring import mark_safe
from SystemDesign.utility import SVGAndImageField
from django.db import models
from django.template.defaultfilters import truncatechars
# Create your models here.


class Problem(models.Model):
    name = models.CharField(name='name', verbose_name="Problem Name", db_column="name", max_length=500)
    description = models.TextField(name='description', verbose_name="Problem Description", db_column="description", max_length=5000)
    image = SVGAndImageField(name='image', verbose_name='image', upload_to='problem')

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"
        db_table = "problem"

    def custom_description(self):
        return truncatechars(self.description, 150)

    custom_description.short_description = "description"
    custom_description.allow_tags = True

    def custom_image_field(self):
        return mark_safe('<img src="{}" width=50 height=50/>'.format(self.image.url))
    
    custom_image_field.short_description = 'Image'
    custom_image_field.allow_tags = True

    def __str__(self):
        return "{}".format(self.name)
