from django.forms import ClearableFileInput

from core.forms import AbstractModelForm
from posts.models import Posts


class AddCatForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'gallery',
            'status',
            'cat_color',
            'cat_breed',
            'gender',
            'wool_type',
            'socialization',
            'health',
            'age',
        )
        widgets = {
            'gallery': ClearableFileInput(attrs={'multiple': True}),
        }


class AddDogForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'gallery',
            'status',
            'dog_color',
            'gender',
            'size',
            'wool_type',
            'socialization',
            'health',
            'age',
        )
        widgets = {
            'gallery': ClearableFileInput(attrs={'multiple': True}),
        }


class AddOtherForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'gallery',
            'status',
            'other_animal_type',
        )
        widgets = {
            'gallery': ClearableFileInput(attrs={'multiple': True}),
        }


class CatFilterForm(AbstractModelForm):
    class Meta:
        model = Posts

        fields = (
            'cat_color',
            'cat_breed',
            'gender',
            'wool_type',
            'socialization',
            'health',
            'age',
        )


class DogFilterForm(AbstractModelForm):
    class Meta:
        model = Posts

        fields = (
            'dog_color',
            'gender',
            'size',
            'wool_type',
            'socialization',
            'health',
            'age',
        )


class OtherFilterForm(AbstractModelForm):
    class Meta:
        model = Posts

        fields = (
            'other_animal_type',
        )
