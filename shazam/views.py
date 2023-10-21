from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("you must Be logged In to see this page..."))
        return redirect('home')
