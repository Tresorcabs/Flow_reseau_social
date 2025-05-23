from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # connexion auto après inscription
            messages.success(request, "inscription réussie")
            print("Inscription réussie")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})



@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            print("Profil mis à jour avec succès")
            return redirect('edit-profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})