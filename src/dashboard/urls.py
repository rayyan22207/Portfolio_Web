from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('projects/', views.projects, name='projects'),
    path ('contact/', views.contact, name='contact'),
    path('note/', views.note, name='note'),
    path('blog/', views.blog, name='blog'),
]
