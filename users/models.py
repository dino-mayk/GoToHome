from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail, delete
from django_cleanup.signals import cleanup_pre_delete

from users.managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        'username',
        max_length=150,
    )
    city = models.CharField(
        'city',
        max_length=150,
        default='Пермь',
    )
    email = models.EmailField(
        'email address',
        unique=True
    )

    IS_SHELTER_TYPES = [
        (False, 'Пользователь'),
        (True, 'Приют'),
    ]

    is_shelter = models.BooleanField(
        verbose_name='Приют или посетитель',
        choices=IS_SHELTER_TYPES,
        default=False,
    )

    avatar = models.ImageField(upload_to='uploads/avatars/%Y/%m',
                               verbose_name='Аватар',
                               help_text='загрузите картинку',
                               default='default_avatar.jpg'
                               )

    @property
    def get_img(self):
        return get_thumbnail(self.avatar, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.avatar:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
