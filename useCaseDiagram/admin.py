from django.contrib import admin
from .models import Actors, UseCaseDiagram, UseCases, ActorSubtask, SubUsecase


# Register your models here.


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    fields = ("usecasediagram", "actor",)
    list_display = ("usecasediagram", "custom_actor",)
    list_display_links = ("usecasediagram", "custom_actor",)


@admin.register(UseCaseDiagram)
class UseCaseDiagramAdmin(admin.ModelAdmin):
    fields = ("problem", "image",)
    list_display = ("problem", "custom_image_field",)
    list_display_links = ("problem", "custom_image_field",)


@admin.register(UseCases)
class UseCasesAdmin(admin.ModelAdmin):
    fields = ("usecasediagram", "use_case",)
    list_display = ("usecasediagram", "custom_usecase",)
    list_display_links = ("usecasediagram", "custom_usecase",)


@admin.register(ActorSubtask)
class ActorSubtaskAdmin(admin.ModelAdmin):
    list_display = ("actor", "value",)
    list_display_links = ("actor", "value",)


@admin.register(SubUsecase)
class SubUsecaseAdmin(admin.ModelAdmin):
    list_display = ("usecase", "value",)
    list_display_links = ("usecase", "value",)
