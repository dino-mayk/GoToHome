from django.shortcuts import render
from django.contrib import messages

from .models import Posts
from .forms import PostsForms


def posts_list(request):
    template_name = 'posts/posts_list.html'
    posts = Posts.objects.homepage()
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)


def post_details(request):
    pass


def add_post(request):
    form = PostsForms(request.POST or None)

    template_name = 'posts/add_post.html'

    context = {
        'form': form,
    }
    print(request.method)
    if request.method == 'POST':
        title, text, photo = request.POST.get('title'), \
                             request.POST.get('text'), \
                             request.POST.get('photo')
        print(title, text, photo)
        Posts.objects.create(title=title, text=text, photo=photo,
                             user=request.user)
        messages.success(request, 'Ваш пост был успешно создан')

    return render(request, template_name, context)
