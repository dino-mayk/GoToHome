from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', )


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
