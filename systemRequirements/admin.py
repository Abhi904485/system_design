from django.contrib import admin
from .models import SystemRequirement
# Register your models here.


@admin.register(SystemRequirement)
class SystemRequirementAdmin(admin.ModelAdmin):
    class Meta:
        model = SystemRequirement
    list_display = ('problem', 'requirement',)
    list_display_links = ('problem', 'requirement',)
