from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def dashboard_view(request):
    return render(request, "dashboard/main.html", {})

def about(request):
    return render(request, 'dashboard/about.html')