from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'dashboard/projects.html', {'projects': all_projects})


def dashboard_view(request):
    return render(request, "dashboard/main.html", {})

def contact(request):
    return render(request, 'dashboard/contact.html')

def note(request):
    return render(request, "dashboard/note.html", {})

def blog(request):
    return render(request, "dashboard/blog.html", {})