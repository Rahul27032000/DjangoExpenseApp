from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    print(user)
    context={'profile': profile}
    return render(request, 'home/home.html',context)
