from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
def home(request):
    Projects = Project.objects.all()
    return render(request, 'post/main.html', {'Projects' : Projects})