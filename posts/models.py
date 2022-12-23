from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField

from posts.managers import FavManager, PostsManager
from users.models import CustomUser


class Posts(models.Model):
    user = models.ForeignKey(
        CustomUser(),
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='выберете пользователя',
    )
    title = models.CharField(
        'Заголовок',
        max_length=150,
    )
    text = HTMLField(
        verbose_name='описание',
        help_text='введите ваше описание поста',
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='возраст',
        default=0,
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='загрузите картинку',
        null=True,
    )
    ANIMAL_TYPES = [
        (1, 'Кошка'),
        (2, 'Собака'),
        (3, 'Другое'),
    ]
    STATUS_TYPES = [
        (True, 'Пост активен'),
        (False, 'Пост приостановлен'),
    ]
    animal_type = models.PositiveSmallIntegerField(
        verbose_name='тип животного',
        choices=ANIMAL_TYPES,
        default=3,
    )
    status = models.BooleanField(
        verbose_name='статус поста',
        choices=STATUS_TYPES,
        default=True,
    )
    objects = PostsManager()

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '300x300',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
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
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Favourites(models.Model):
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name='пост',
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='пользователь',
    )
    objects = FavManager()

    def __str__(self):
        return f'{self.user} - {self.post}'

    class Meta:
        verbose_name = 'избранный пост'
        verbose_name_plural = 'избранные посты'
