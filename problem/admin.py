from django.contrib import admin
from .models import Problem


# Register your models here.


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    class Meta:
        model = Problem

    fields = ('name', 'description', 'image',)
    list_display = ('name', 'custom_description', 'custom_image_field',)
    list_display_links = ('name', 'custom_description', 'custom_image_field',)
