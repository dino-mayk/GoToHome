from posts.models import Posts
from core.forms import AbstractModelForm


class AddCatForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'status',
            'cat_color',
            'cat_breed',
            'gender',
            'wool_type',
            'socialization',
            'health',
            'age',
        )


class AddDogForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'status',

            'dog_color',
            'gender',
            'size',
            'wool_type',
            'socialization',
            'health',
            'age',
        )


class AddOtherForm(AbstractModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'status',
            'other_animal_type',
        )


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
