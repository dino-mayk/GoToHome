from django.shortcuts import render

from posts.forms import CatFilterForm, DogFilterForm, OtherFilterForm
from posts.models import Posts


def home(request, filter=None):
    if filter:
        posts = Posts.objects.homepage().filter(animal_type=filter)
    else:
        posts = Posts.objects.homepage()

    cat_form = CatFilterForm(request.POST)
    dog_form = DogFilterForm(request.POST)
    other_form = OtherFilterForm(request.POST)

    context = {
        'posts': posts,
        'animal_types': Posts.ANIMAL_TYPES,
        'cat_form': cat_form,
        'dog_form': dog_form,
        'other_form': other_form,
    }
    return render(request, 'homepage/index.html', context)
