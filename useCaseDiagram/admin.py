from django.contrib import admin
from .models import Actors, UseCaseDiagram, UseCases
# Register your models here.



@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    class Meta:
        model = Actors
   
    fields = ("usecasediagram", "actor",)
    list_display = ("custom_actor",)
    list_display_links = ("custom_actor",)


@admin.register(UseCaseDiagram)
class UseCaseDiagramAdmin(admin.ModelAdmin):
    class Meta:
        model = UseCaseDiagram
    fields = ("problem", "image",)
    list_display = ("custom_image_field",)
    list_display_links = ("custom_image_field",)


@admin.register(UseCases)
class UseCasesAdmin(admin.ModelAdmin):
    class Meta:
        model = UseCases

    fields = ("usecasediagram","use_case",)
    list_display = ("custom_usecase",)
    list_display_links = ("custom_usecase",)
