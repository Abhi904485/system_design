from django.contrib import admin
from .models import Actors, UseCaseDiagram, UseCases
# Register your models here.
admin.site.register(Actors)
admin.site.register(UseCaseDiagram)
admin.site.register(UseCases)
