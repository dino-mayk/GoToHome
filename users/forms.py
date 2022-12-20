from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import CustomUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',
                  'email', 'password1', 'password2', 'is_shelter', 'avatar')
        labels = {
            CustomUser.username.field.name: 'Имя пользователя',
            CustomUser.avatar.field.name: 'аватарка'
        }


class CustomUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
        )
        labels = {
            'first_name': 'Имя',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
