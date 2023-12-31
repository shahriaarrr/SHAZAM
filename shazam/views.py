from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Profile, Thunder
from .forms import ThunderForm, SignUpForm, UserUpdateForm, ProfilePicForm


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
        thunders = Thunder.objects.filter(user_id=pk).order_by("-created_at")

        # post form
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


def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Authenticate and log in the user
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            messages.success(request, "Your signup was successful⚡. Welcome to the club, Hunter👋")
            return redirect('home')

    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, (f"Welcome back {username}👋, let's hunt :)"))
            return redirect('home')
        else:
            messages.error(request, ("♻️There was an error in your username or password. please try again♻️"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth_logout(request)
    messages.success(request, ("Goodbye Hunter, see you soon..."))
    return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            auth_login(request, current_user)
            messages.success(request, "🎉 Your profile has been updated 🎉")
            return redirect('home')

        return render(request, "update_user.html", {'user_form': user_form, 'profile_form': profile_form})
    else:
        messages.error(request, "You must be logged in to see this page.")
        return redirect('home')


def thunder_likes(request, pk):
    if request.user.is_authenticated:
        thunder = get_object_or_404(Thunder, id=pk)

        if thunder.likes.filter(id=request.user.id).exists():
            thunder.likes.remove(request.user)
        else:
            thunder.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))

    else:
        messages.error(request, "You must be logged in to like thunders.")
        return redirect('home')


def thunder_show(request, pk):
    thunder = get_object_or_404(Thunder, id=pk)

    if thunder:
        return render(request, 'show_thunder.html', {'thunder':thunder})
    else:
        messages.error(request, "That thunder dose not exist💀")
        return redirect('home')


def delete_thunder(request, pk):
    if request.user.is_authenticated:
        thunder = get_object_or_404(Thunder, id=pk)
        if request.user.username == thunder.user.username:
            thunder.delete()
            messages.success(request, "the thunder has been deleted👍.")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "that's not your thunder.")
            return redirect('home')

    else:
        messages.error(request, "You must be logged in to do this action.")
        return redirect(request.META.get('HTTP_REFERER'))


def hunt(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=pk)
        request.user.profile.hunters.add(profile)
        request.user.profile.save()

        messages.success(request, f"You have successfully hunt {profile.user.username}")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "You must be logged in to do this action.")
        return redirect('home')


def unhunt(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=pk)
        request.user.profile.hunters.remove(profile)
        request.user.profile.save()

        messages.success(request, f"You have successfully unhunt {profile.user.username}")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "You must be logged in to do this action.")
        return redirect('home')


def hunters(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:

            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'hunters.html', {"profiles": profiles})
        else:
            messages.error(request, ("That's not your profile page..."))
            return redirect('home')
    else:
        messages.error(request, ("you must Be logged In to see this page..."))
        return redirect('home')


def hunts(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:

            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'hunts.html', {"profiles": profiles})
        else:
            messages.error(request, ("That's not your profile page..."))
            return redirect('home')
    else:
        messages.error(request, ("you must Be logged In to see this page..."))
        return redirect('home')
