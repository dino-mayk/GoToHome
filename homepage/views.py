from django.shortcuts import render

from posts.models import Posts

def home(request, filter=None):
    if filter:
        posts = Posts.objects.homepage().filter(animal_type=filter)
    else:
        posts = Posts.objects.homepage()
    context = {
        'posts': posts,
        'animal_types': Posts.ANIMAL_TYPES,
    }
    return render(request, 'homepage/index.html', context)


def map(request):
    template_name = 'maps/shelter_maps.html'

    return render(request, template_name)
