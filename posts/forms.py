from django.forms import ModelForm

from posts.models import Posts


class AddCatForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

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


class AddDogForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

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


class AddOtherForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
            'photo',
            'status',

            'other_animal_type',
        )


class CatFilterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

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


class DogFilterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

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


class OtherFilterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Posts

        fields = (
            'other_animal_type',
        )
