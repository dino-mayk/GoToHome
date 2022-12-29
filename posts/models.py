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
        'заголовок',
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
        null=True,
    )

    ANIMAL_TYPES = [
        (1, 'Кошка'),
        (2, 'Собака'),
        (3, 'Другое'),
    ]

    CAT_COLORS = [
        (100, '---'),
        (1, 'белый'),
        (2, 'серый'),
        (3, 'рыжий'),
        (4, 'черный'),
        (5, 'черепаховый'),
        (6, 'трехцветный'),
        (7, 'бело-черный'),
        (8, 'бело-рыжий'),
        (9, 'бело-серый'),
        (10, 'рыже-черный'),

    ]

    DOG_COLORS = [
        (100, '---'),
        (1, 'белый'),
        (2, 'серый'),
        (3, 'рыжий'),
        (4, 'черный'),
        (5, 'черепаховый'),
        (6, 'трехцветный'),
        (7, 'бело-черный'),
        (8, 'бело-рыжий'),
        (9, 'бело-серый'),
        (10, 'рыже-черный'),

    ]

    WOOL_TYPES = [
        (100, '---'),
        (1, 'короткошерстная'),
        (3, 'среднешерстная'),
        (2, 'длинношерстная'),

    ]

    AGE_RANGES = [
        (100, '---'),
        (1, 'до 1 года'),
        (2, 'от 1 до 2 лет'),
        (3, 'от 2 до 5 лет'),
        (4, 'от 5 до 8 лет'),
        (5, 'от 8-11 лет'),
        (6, 'свыше 11 лет'),

    ]

    CAT_BREEDS = [
        (100, '---'),
        (1, 'породистый'),
        (2, 'без породы'),

    ]

    SOCIALIZATION_LEVEL = [
        (100, '---'),
        (1, 'высокая'),
        (2, 'средняя'),
        (3, 'низкая'),
    ]

    HEALTH_CONDITIONS = [
        (100, '---'),
        (1, 'без особенностей'),
        (2, 'с особенностями'),

    ]

    GENDERS = [
        (100, '---'),
        (1, 'мужской'),
        (2, 'женский'),

    ]

    DOG_SIZES = [
        (100, '---'),
        (1, 'мелкий'),
        (2, 'средний'),
        (3, 'крупный'),

    ]

    OTHER_ANIMALS_TYPES = [
        (100, '---'),
        (1, 'хомяк'),
        (2, 'кролик'),
        (3, 'морская свинка'),
        (4, 'птицы'),
        (5, 'змеи'),

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

    cat_color = models.PositiveSmallIntegerField(
        verbose_name='цвет кошки',
        choices=CAT_COLORS,
        default=100,
    )

    dog_color = models.PositiveSmallIntegerField(
        verbose_name='цвет собаки',
        choices=DOG_COLORS,
        default=100,
    )

    age = models.PositiveSmallIntegerField(
        verbose_name='возраст',
        choices=AGE_RANGES,
        default=100,
    )

    cat_breed = models.PositiveSmallIntegerField(
        verbose_name='порода кошки',
        choices=CAT_BREEDS,
        default=100,
    )

    size = models.PositiveSmallIntegerField(
        verbose_name='размер животного',
        choices=DOG_SIZES,
        default=100,
    )

    gender = models.PositiveSmallIntegerField(
        verbose_name='пол животного',
        choices=GENDERS,
        default=100,
    )

    wool_type = models.PositiveSmallIntegerField(
        verbose_name='тип шерсти',
        choices=WOOL_TYPES,
        default=100,
    )

    socialization = models.PositiveSmallIntegerField(
        verbose_name='уровень социализации',
        choices=SOCIALIZATION_LEVEL,
        default=100,
    )

    health = models.PositiveSmallIntegerField(
        verbose_name='состояние здоровья',
        choices=HEALTH_CONDITIONS,
        default=100,
    )

    other_animal_type = models.PositiveSmallIntegerField(
        verbose_name='тип животного',
        choices=OTHER_ANIMALS_TYPES,
        default=100,
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
