from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Classes, Assignments
from allauth.socialaccount.models import SocialAccount



# Create your views he re.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        picture = extra_data['picture']
        username = request.user
        form = Classes.objects.all()
        #profile_pic=user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
        #username=user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
        context = {'form':form,'username':username, 'user_image': picture}
        return render(request, 'home.html', context)

class Login(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class Classroom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = Classes.objects.all()
        class_id = request.GET.get('class')
        username = request.user
        class_assignment = Assignments.objects.all().filter(class_id=class_id)
        class_details = Classes.objects.all().filter(class_id=class_id)
        context = {'username':username, 'class_id': class_id, 'assignments': class_assignment, 'class_details': class_details}
        return render(request, 'classroom.html',context)