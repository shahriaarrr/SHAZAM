from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from .models import Profile, Thunder
from .forms import ThunderForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        form = ThunderForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                thunder = form.save(commit=False)
                thunder.user = request.user
                thunder.save()

                messages.success(request, ("⚡Your thunder has been successfully struck⚡"))

                return redirect('home')


        thunders = Thunder.objects.all().order_by("-created_at")
        return render(request, 'home.html', {'thunders': thunders, 'form': form})
    else:
        thunders = Thunder.objects.all().order_by("-created_at")
        return render(request, 'home.html', {'thunders': thunders})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("you must Be logged In to see this page..."))
        return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        thunders = Thunder.objects.filter(user_id=pk)

        #post form
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['hunt']

            if action == "unhunt":
                current_user_profile.hunters.remove(profile)
            else:
                current_user_profile.hunters.add(profile)

            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile, 'thunders': thunders})
    else:
        messages.success(request, ("you must Be logged In to see this page..."))
        return redirect('home')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, (f"Welcome back {username}, let's hunt :)"))
            return redirect('home')
        else:
            messages.error(request, (f"There was an error in your username or password. please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html', {})
