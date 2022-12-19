from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.models import update_attrs

from .forms import PostsForms
from .models import Favourites, Posts


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

    if not request.user.is_shelter:
        return redirect('posts:posts_list')

    form = PostsForms(request.POST, request.FILES,)

    template_name = 'posts/add_post.html'

    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title')
        text = form.cleaned_data.get('text')
        age = form.cleaned_data.get('age')

        photo = form.cleaned_data.get('photo')
        animal_type = form.cleaned_data.get('animal_type')
        new_post = Posts.objects.create(
            title=title,
            text=text,
            photo=photo,
            age=age,
            animal_type=animal_type,
            user=request.user
        )
        new_post.save()
        messages.success(request, 'Ваш пост был успешно создан')
        return redirect('homepage:home')

    return render(request, template_name, context)


def edit_post(request, pk):

    curr_post = get_object_or_404(Posts, pk=pk)
    form = PostsForms(data=request.POST, instance=curr_post)
    template_name = 'posts/edit_post.html'

    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        update_attrs(curr_post, **form.cleaned_data)
        messages.success(request, 'Пост был успешно обновлен')

    return render(request, template_name, context)


def delete_post(request, pk):
    pass
