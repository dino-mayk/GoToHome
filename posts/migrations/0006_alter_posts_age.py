# Generated by Django 3.2.16 on 2022-12-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20221229_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='age',
            field=models.PositiveSmallIntegerField(choices=[(1, 'до 1 года'), (2, 'от 1 до 2 лет'), (3, 'от 2 до 5 лет'), (4, 'от 5 до 8 лет'), (5, 'от 8-11 лет'), (6, 'свыше 11 лет')], default=1, verbose_name='возраст'),
        ),
    ]
