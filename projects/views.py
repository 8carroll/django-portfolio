from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse

# Create your views here.
def all_projects(request):
    # query db to return all projects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/details.html',
                  {'project': project})
