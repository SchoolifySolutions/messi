from django.contrib import admin
from .models import Classes, Assignments, UserClassData, UserAssignmentData

# Register your models here.
admin.site.register(Classes)
admin.site.register(Assignments)
admin.site.register(UserClassData)
admin.site.register(UserAssignmentData)