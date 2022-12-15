from django.shortcuts import render

from posts.models import Posts

def home(request):

    posts = Posts.objects.homepage()

    context = {
        'posts': posts,
    }
    return render(request, 'homepage/index.html', context)
