from django.contrib import admin
from .models import ClassDiagram , Class
# Register your models here.

@admin.register(ClassDiagram)
class ClassDiagramAdmin(admin.ModelAdmin):
    class Meta:
        model = ClassDiagram
        fields = '__all__'
    list_display = ('problem','custom_image_field', 'custom_uml_field', )
    list_display_links = ('problem','custom_image_field', 'custom_uml_field', )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    class Meta:
        model = Class
        fields = '__all__'
    list_display = ('class_diagram','name',)
    list_display_links = ('class_diagram','name',)
