from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Favourites, Posts
from users.forms import CustomUserProfileForm, CustomUserSignUpForm, LoginForm
from users.models import CustomUser


class Login(LoginView):
    form_class = LoginForm


def signup(request):
    form = CustomUserSignUpForm(data=request.POST, files=request.FILES)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        messages.success(request, 'Вы успешно зарегистрировались')
        login(request, user)
        return redirect('homepage:home')
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(data=request.POST, files=request.FILES,
                                     instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = CustomUserProfileForm(instance=request.user)

    if request.user.is_shelter:
        profile_posts = Posts.objects.filter(user=request.user)
    else:
        profile_posts = Posts.objects.filter(
            pk__in=Favourites.objects.get_user_fav_posts(
                user=request.user
            )
        )
    context = {
        'form': form,
        (
            'posts_mine' if request.user.is_shelter else 'posts_fav'
        ): profile_posts,
    }
    return render(request, 'users/profile.html', context)


def shelter_profile(request, pk):
    form = CustomUserProfileForm(instance=request.user)

    shelter = get_object_or_404(CustomUser, pk=pk)
    shelter_posts = Posts.objects.filter(user__id=pk)

    context = {
        'form': form,
        'shelter_posts': shelter_posts,
        'shelter': shelter,
    }
    return render(request, 'users/shelter_profile.html', context)
