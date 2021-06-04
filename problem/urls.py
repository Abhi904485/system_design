from django.urls import path
from .views import problems

app_name = "problem"
urlpatterns = [
    path("<int:problem_id>/", problems, name="problem")
]
