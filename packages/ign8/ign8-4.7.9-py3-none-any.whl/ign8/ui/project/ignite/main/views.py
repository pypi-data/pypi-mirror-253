from django.shortcuts import render
from .models import maindata, service, project
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets


@csrf_exempt
def mainview(request):
    maindata_entries = maindata.objects.all()
    maindata_services = service.objects.all()
    maindata_projects = project.objects.all()
    return render(request, 'main.html', {'maindata_entries': maindata_entries, 'title': 'IGN8', 'maindata_services': maindata_services , 'maindata_projects': maindata_projects})

@csrf_exempt
def projectsview(request):
    myprojects = project.objects.all()
    return render(request, 'projects.html', {'maindata_entries': myprojects, 'title': 'Projects'})

@csrf_exempt
def projectdetail(request, name=None):
    if name:
        myproject = project.objects.get(name=name)
    else:
        myproject = project.objects.all()
    return render(request, 'projectdetail.html', {'projects': myproject, 'title': 'Project Detail'})    

