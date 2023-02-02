from django.db import models
from datetime import datetime

# Create your models here.
class Classes(models.Model):
    class_id = models.CharField(max_length=8,null=False, primary_key=True)
    class_subject = models.CharField(max_length=12,null=False)
    class_name = models.CharField(max_length=30,null=False)
    teacher_name = models.CharField(max_length= 30,null=False)
    assignments_due = models.IntegerField()
    def __str__(self):
         return self.class_name

class Assignments(models.Model):
    assignments_name = models.CharField(max_length=120,null=False)
    assignment_description = models.CharField(max_length=800,null=False)
    class_id = models.CharField(max_length=8,null=False)
    active = models.BooleanField(default=True)
    due_date = models.DateTimeField(null=False)
    date_created = models.DateField(default = datetime.now())
    def __str__(self):
        return self.assignments_name

class UserClassData(models.Model):
    user_id = models.CharField(max_length=8,null=False)
    class_id = models.CharField(max_length=8,null=False)
    def __str__(self):
        return self.user_id 