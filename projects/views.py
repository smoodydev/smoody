from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def all_projects(request):
    category = language = None
    projects = Project.objects.all()
    if request.GET:
        if "categories" in request.GET:
            categories = request.GET["categories"].split(',')
            projects = projects.filter(categories__url_safe__in=categories)


    return render(request, "all_projects.html", {"projects":projects})


def project(request, pid):
    project = get_object_or_404(Project, pk=pid)
    print(project)
    return render(request, "project.html", {"project": project})