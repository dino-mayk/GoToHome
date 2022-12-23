from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.models import update_attrs
from posts.forms import PostsForms
from posts.models import Favourites, Posts


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
    fav = Favourites.objects.get_user_and_post(
        user=request.user,
        post=curr_post,
    )
    if request.method == 'POST' and not request.user.is_shelter:
        if fav.exists():
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
        new_post = Posts.objects.create(
            user=request.user,
            **form.cleaned_data
        )
        new_post.save()
        messages.success(request, 'Ваш пост был успешно создан')
        return redirect('users:profile')
    return render(request, template_name, context)


def edit_post(request, pk):
    curr_post = get_object_or_404(Posts, pk=pk)
    form = PostsForms(
        data=request.POST,
        files=request.FILES,
        instance=curr_post
    )
    template_name = 'posts/edit_post.html'
    context = {
        'form': form,
    }
    if request.user.id != curr_post.user.id:
        messages.error(request, 'У вас нет доступа к чужому посту')
        return redirect('homepage:home')
    if request.method == 'POST' and form.is_valid():
        update_attrs(curr_post, **form.cleaned_data)
        messages.success(request, 'Пост был успешно обновлен')
        return redirect('users:profile')
    return render(request, template_name, context)


def delete_post(request, pk):
    template_name = 'posts/delete_post.html'
    post_to_delete = get_object_or_404(Posts, pk=pk)
    context = {
        'post': post_to_delete,
    }
    if request.user.id != post_to_delete.user.id:
        messages.error(request, 'У вас нет доступа к чужому посту')
        return redirect('homepage:home')
    if request.POST:
        post_to_delete.delete()
        messages.success(request, 'Ваш пост успешно удален')
        return redirect('users:profile')
    return render(request, template_name, context)
