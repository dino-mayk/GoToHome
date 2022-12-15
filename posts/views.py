from django.shortcuts import render, redirect
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


def post_details(request, pk):
    template_name = 'posts/post_detail.html'
    print(pk)
    post = Posts.objects.get(pk=pk)
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
