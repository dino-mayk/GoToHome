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
    if request.method == 'POST':
        form = CustomUserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            password = form.cleaned_data.get('password1')

            user = authenticate(email=user.email, password=password)
            login(request, user)

            return redirect('homepage:home')
    form = CustomUserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})


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
        posts = Posts.objects.filter(user=request.user)
    else:
        posts = Posts.objects.filter(
            pk__in=Favourites.objects.get_user_fav_posts(
                user=request.user
            )
        )
    context = {
        'form': form,
        'fav_posts': posts,
    }
    return render(request, 'users/profile.html', context)
