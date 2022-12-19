from django.contrib import messages
from django.shortcuts import redirect, render

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

    try:
        fav = Favourites.objects.get_user_and_post(
            user=request.user,
            post=curr_post,
        )
        if request.method == 'POST' and fav.exists():
            fav.delete()
            messages.info(request, 'Больше не в избранных')
        else:
            Favourites.objects.create(
                user=request.user,
                post=curr_post,
            )
            messages.info(request, 'Добавлено в избранные')
        context = {
            'post': post,
            'is_fav': fav.exists(),
        }
    except TypeError:
        context = {
            'post': post,
        }

    return render(request, template_name, context)


def add_post(request):
    form = PostsForms(request.POST, request.FILES,)

    template_name = 'posts/add_post.html'

    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title')
        text = form.cleaned_data.get('text')
        photo = form.cleaned_data.get('photo')
        animal_type = form.cleaned_data.get('animal_type')
        new_post = Posts.objects.create(
            title=title,
            text=text,
            photo=photo,
            animal_type=animal_type,
            user=request.user,
        )
        new_post.save()
        messages.success(request, 'Ваш пост был успешно создан')
        return redirect('homepage:home')

    return render(request, template_name, context)
