from django.forms import ModelForm

from posts.models import Posts


class PostsForms(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Posts
        fields = (
            Posts.title.field.name,
            Posts.text.field.name,
            Posts.age.field.name,
            Posts.photo.field.name,
            Posts.animal_type.field.name,
            Posts.status.field.name,
        )
        labels = {
            Posts.title.field.name: 'Заголовок',
            Posts.text.field.name: 'Текст',
            Posts.age.field.name: 'Возраст животного',
            Posts.photo.field.name: 'Фото',
            Posts.animal_type.field.name: 'Тип животного',
            Posts.status.field.name: 'Статус поста',
        }
