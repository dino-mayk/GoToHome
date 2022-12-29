from django.shortcuts import render

from posts.forms import CatFilterForm, DogFilterForm, OtherFilterForm
from posts.models import Posts


def home(request):
    cat_form = CatFilterForm(request.POST)
    dog_form = DogFilterForm(request.POST)
    other_form = OtherFilterForm(request.POST)

    if request.method == 'POST':
        if 'dog_color' in request.POST and dog_form.is_valid():

            filter_dict = {}
            for value in dog_form.cleaned_data:
                if dog_form.cleaned_data[value] != 100:
                    filter_dict[value] = dog_form.cleaned_data[value]

            posts = Posts.objects.dogfilter(**filter_dict)

        elif 'cat_color' in request.POST and cat_form.is_valid():

            filter_dict = {}
            for value in cat_form.cleaned_data:
                if cat_form.cleaned_data[value] != 100:
                    filter_dict[value] = cat_form.cleaned_data[value]

            posts = Posts.objects.catfilter(**cat_form.cleaned_data)

        elif 'other_animal_type' in request.POST and other_form.is_valid():

            filter_dict = {}
            for value in other_form.cleaned_data:
                if other_form.cleaned_data[value] != 100:
                    filter_dict[value] = other_form.cleaned_data[value]

            posts = Posts.objects.otherfilter(**other_form.cleaned_data)
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
