from django.urls import path
from .views import all_projects, project

urlpatterns = [
    path("", all_projects, name="all_projects"), 
    path("<pid>", project, name="project")
]