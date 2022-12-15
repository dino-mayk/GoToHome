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
        verbose_name='автор',
        help_text='выберете пользователя',
    )
    title = models.CharField(
        'Заголовок',
        max_length=150,
    )
    text = HTMLField(
        verbose_name='Описание',
        help_text='введите ваше описание поста',
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='Картинка',
        help_text='загрузите картинку',
    )
    map_long = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=59.,
        blank=True,
        null=True,
    )
    map_lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=59.,
        blank=True,
        null=True,
    )

    ANIMAL_TYPES = [
        (1, 'Кошка'),
        (2, 'Собака'),
        (3, 'Другое'),
    ]
    animal_type = models.PositiveSmallIntegerField(
        verbose_name='Тип животного',
        choices=ANIMAL_TYPES,
        default=3
    )


    objects = PostsManager()

    @property
    def get_img(self):
        return get_thumbnail(self.photo, '300x300', crop='center', quality=51)

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
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
