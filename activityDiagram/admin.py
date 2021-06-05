from django.contrib import admin
from django.utils.html import format_html
from .models import ActivityDiagram

# Register your models here.


@admin.register(ActivityDiagram)
class Admin(admin.ModelAdmin):
    fields = ('problem', 'activity', 'image')
    list_display = ('activity', 'custom_image_field')
    list_display_links = ('activity', 'custom_image_field')
