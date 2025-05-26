from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import UserRegisterForm, ProfileUpdateForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Follow, Profile, Post
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.


# -> Vue d'accueil
@login_required
def home(request):
    # 🔎 Profils déjà suivis
    followed_users = Follow.objects.filter(follower=request.user).values_list('following__id', flat=True)

    # 🎯 Suggestions : utilisateurs à recommander (non suivis et différent de soi)
    suggestions = User.objects.exclude(
        Q(id__in=followed_users) | Q(id=request.user.id)
    )[:5]  # Limite les suggestions à 5, modifiable

    # 📬 Gestion du formulaire de post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Votre post a été publié.")
            return redirect('home')
        else:
            messages.error(request, "Une erreur s'est produite lors de la publication.")
    else:
        form = PostForm()

    # 📰 Posts récents à afficher
    posts = Post.objects.all().order_by('-created_at')[:10]  # Plus que 5 si tu veux scroller un peu

    return render(request, 'core/home.html', {
        'suggestions': suggestions,
        'posts': posts,
        'form': form,
    })


# -> Vue d'inscription

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


# -> Vue vers le profile
@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    profile = user_profile.profile
    is_following = False

    if request.user.is_authenticated and request.user != user_profile:
        is_following = Follow.objects.filter(follower=request.user, following=user_profile).exists()

    followers_count = Follow.objects.filter(following=user_profile).count()
    following_count = Follow.objects.filter(follower=user_profile).count()

    context = {
        'user_profile': user_profile,
        'profile': profile,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    
    return render(request, 'core/profile.html', context)

 
# -> Vue d'édition du profil
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            form.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})

# -> Vue de Follow
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        messages.success(request, f'Vous suivez maintenant {user_to_follow.username}')
        print(f'Vous suivez maintenant {user_to_follow.username}')
    return redirect('profile', username=username)

# -> Vue de Unfollow
@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    messages.success(request, f'Vous ne suivez plus {user_to_unfollow.username}')
    print(f'Vous ne suivez plus {user_to_unfollow.username}')
    return redirect('profile', username=username)

# -> Vue pour la création de post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            messages.success(request, 'Post publié avec succès.')
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})