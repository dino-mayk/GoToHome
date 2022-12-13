from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField

from posts.managers import PostsManager
from users.models import CustomUser


class Posts(models.Model):
    user = models.ForeignKey(
        CustomUser(),
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        help_text='выберете пользователя',
    )
    name = models.CharField(
        'name',
        max_length=150,
    )
    text = HTMLField(
        verbose_name='описание',
        help_text='введите ваше описание поста',
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='загрузите картинку',
    )
    map_long = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )
    map_lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )
    is_favourites = models.BooleanField(
        default=False,
        verbose_name='в избранном',
    )
    objects = PostsManager()

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = 'превью поста'
        verbose_name_plural = 'превьюшки постов'
