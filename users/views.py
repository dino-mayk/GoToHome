from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import View

from users.forms import CustomUserProfileForm, CustomUserSignUpForm


class Signup(View):
    def post(self, request):
        form = CustomUserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            password = form.cleaned_data.get('password1')

            user = authenticate(email=user.email, password=password)
            login(request, user)

            return redirect('homepage:home')
        return redirect('users:login')

    def get(self, request):
        form = CustomUserSignUpForm()
        return render(request, 'users/signup.html', {'form': form})


class Profile(View):
    def post(self, request):
        try:
            form = CustomUserProfileForm(
                request.POST or None,
                instance=request.user)
            form.save()
        except ValueError:
            pass
        return render(request, 'users/profile.html', {'form': form})

    def get(sekf, request):
        form = CustomUserProfileForm(
            request.POST or None,
            instance=request.user)
        return render(request, 'users/profile.html', {'form': form})
