from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class CustomUser(AbstractUser):
    objects = UserManager()
    username = models.CharField('username', max_length=150)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']