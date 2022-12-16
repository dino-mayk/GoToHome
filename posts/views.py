from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models

from .models import Posts, Favourites
from .forms import PostsForms


def posts_list(request):
    template_name = 'posts/posts_list.html'
    posts = Posts.objects.homepage()
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)


def post_details(request, pk):
    template_name = 'posts/post_detail.html'
    post = Posts.objects.get(pk=pk)
    curr_post = Posts.objects.get(pk=pk)
    fav = Favourites.objects.get_user_and_post(user=request.user,
                                               post=curr_post)
    if request.method == 'POST':
        if fav.exists():
            fav.delete()
            messages.info(request, 'Больше не в избранных')
        else:
            Favourites.objects.create(user=request.user,
                                      post=curr_post)
            messages.info(request, 'Добавлено в избранные')

    context = {
        'post': post,
        'is_fav': fav.exists(),
    }
    return render(request, template_name, context)


def add_post(request):
    form = PostsForms(request.POST, request.FILES,)

    template_name = 'posts/add_post.html'

    context = {
        'form': form,
    }
    print(form.errors, request.FILES)
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title')
        text = form.cleaned_data.get('text')
        photo = form.cleaned_data.get('photo')
        animal_type = form.cleaned_data.get('animal_type')
        print(title, text, photo)
        new_post = Posts.objects.create(title=title, text=text, photo=photo,
                             animal_type=animal_type,
                             user=request.user)
        new_post.save()
        messages.success(request, 'Ваш пост был успешно создан')
        return redirect('homepage:home')

    return render(request, template_name, context)
