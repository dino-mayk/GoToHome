from django.shortcuts import render

from posts.models import Posts

def home(request, filter=None):
    if filter:
        posts = Posts.objects.homepage().filter(animal_type=filter)
    else:
        posts = Posts.objects.homepage()
    context = {
        'posts': posts,
    }
    return render(request, 'homepage/index.html', context)
