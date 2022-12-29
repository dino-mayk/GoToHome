from django.shortcuts import render

from posts.forms import CatFilterForm, DogFilterForm, OtherFilterForm
from posts.models import Posts


def home(request):
    cat_form = CatFilterForm(request.POST)
    dog_form = DogFilterForm(request.POST)
    other_form = OtherFilterForm(request.POST)

    if request.method == 'POST':
        if 'dog_color' in request.POST and dog_form.is_valid():
            posts = Posts.objects.dogfilter(**dog_form.cleaned_data)

        elif 'cat_color' in request.POST and cat_form.is_valid():

            posts = Posts.objects.catfilter()

        elif 'other_color' in request.POST and other_form.is_valid():

            posts = Posts.objects.otherfilter()
    else:
        posts = Posts.objects.homepage()

    context = {
        'posts': posts,
        'animal_types': Posts.ANIMAL_TYPES,
        'cat_form': cat_form,
        'dog_form': dog_form,
        'other_form': other_form,
    }
    return render(request, 'homepage/index.html', context)
