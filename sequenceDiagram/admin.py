from django.contrib import admin
from .models import SequenceDiagram
# Register your models here.


@admin.register(SequenceDiagram)
class SequenceDiagramAdmin(admin.ModelAdmin):
    list_display = ('problem', 'description', 'custom_image_field')
    list_display_links = ('problem', 'description', 'custom_image_field')
