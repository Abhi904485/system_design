from django.contrib import admin

from .models import Codes


# Register your models here.


@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    class Meta:
        model = Codes
        fields = '__all__'

    list_display = ('problem', 'name', 'custom_java', 'custom_python',)
    list_display_links = ('problem', 'name', 'custom_java', 'custom_python',)
