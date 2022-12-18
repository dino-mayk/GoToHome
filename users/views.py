from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from posts.models import Favourites, Posts
from users.forms import CustomUserProfileForm, CustomUserSignUpForm


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
        form = CustomUserProfileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = CustomUserProfileForm(instance=request.user)
    fav_posts = Posts.objects.filter(
        pk__in=Favourites.objects.get_user_fav_posts(user=request.user)
    )
    context = {
        'form': form,
        'fav_posts': fav_posts,
    }
    return render(request, 'users/profile.html', context)
