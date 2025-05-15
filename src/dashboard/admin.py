from django.contrib import admin
from .models import Project, Feedback,Inquiry
# Register your models here.
admin.site.register(Project)
admin.site.register(Inquiry)
admin.site.register(Feedback)