from django.forms import ModelForm

from .models import Posts


class PostsForms(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        fields = (
            Posts.title.field.name,
            Posts.text.field.name,
            Posts.age.field.name,
            Posts.photo.field.name,
            Posts.animal_type.field.name,
        )
        model = Posts
        labels = {
            Posts.title.field.name: 'Заголовок',
            Posts.text.field.name: 'Текст',
            Posts.photo.field.name: 'Фото',
            Posts.animal_type.field.name: 'Тип животного',
            Posts.age.field.name: 'Возраст животного',
        }
