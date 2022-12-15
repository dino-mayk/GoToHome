from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.views import PasswordChangeView

from users.forms import (
    CustomUserProfileForm,
    CustomUserSignUpForm,
    LoginForm,
    PasswordResetForm,
    PasswordChangeForm)


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
        messages.info(request, 'Вы успешно обновили профиль!')
    else:
        form = CustomUserProfileForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})


class Login(LoginView):
    form_class = LoginForm


class PasswordReset(PasswordResetView):
    form_class = PasswordResetForm


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
