from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Classes, Assignments, UserClassData, UserAssignmentData
from allauth.socialaccount.models import SocialAccount



# Create your views here.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        #Get User Data
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        picture = extra_data['picture']
        username = request.user
        #Getting Classroom Information by User
        form = UserClassData.objects.all().filter(user_id=username)
        enrolled_classes = []
        class_objects = []
        for i in form:
            if i in enrolled_classes:
                pass
            else:
                enrolled_classes.append(i.class_id)
        for i in enrolled_classes:
            class_details = Classes.objects.all().filter(class_id=i)
            class_objects.append(class_details)
        #Getting Assignment Information From User
        assignments = UserAssignmentData.objects.values('assignment_id').filter(user_id=username)
        all_assignments = []
        for i in assignments:
            all_assignments.append(Assignments.objects.all().filter(id=i["assignment_id"])) 
            print(all_assignments)
        context = {'form':class_objects,'username':username, 'user_image': picture, 'assignments': all_assignments}
        return render(request, 'home.html', context)

class Login(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class Classroom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = Classes.objects.all()
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        picture = extra_data['picture']
        class_id = request.GET.get('class')
        username = request.user
        class_assignment = Assignments.objects.all().filter(class_id=class_id)
        class_details = Classes.objects.all().filter(class_id=class_id)
        context = {'username':username, 'class_id': class_id, 'assignments': class_assignment, 'class_details': class_details,'user_image': picture}
        return render(request, 'classroom.html',context)