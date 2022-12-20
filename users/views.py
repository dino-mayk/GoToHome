from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, reverse

from posts.models import Favourites, Posts
from users.forms import CustomUserProfileForm, CustomUserSignUpForm, LoginForm


class Login(LoginView):
    form_class = LoginForm


def signup(request):
    form = CustomUserSignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Вы успешно зарегестрировались')
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(instance=request.user)
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
        ('posts_mine' if request.user.is_shelter else 'posts_fav'): profile_posts,
    }
    return render(request, 'users/profile.html', context)
