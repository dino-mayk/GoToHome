from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.forms.models import model_to_dict

from core.models import update_attrs
from posts.forms import AddCatForm, AddDogForm, AddOtherForm
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
    curr_post = Posts.objects.get(pk=pk)
    curr_post_user = curr_post.user
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

    post_dict = model_to_dict(
        curr_post,
        fields=[field.name for field in curr_post._meta.fields]
    )

    for field in Posts._meta.get_fields():
        if hasattr(field, 'choices') and field.choices is not None:
            post_dict[field.name] = dict(field.choices)[post_dict[field.name]]

    context = {
        'post': post_dict,
        'user': curr_post_user,
        'is_fav': fav.exists(),
    }
    return render(request, template_name, context)


def add_post(request, post_type):
    if not request.user.is_shelter:
        return redirect('posts:posts_list')
    if post_type == 'cat':
        form = AddCatForm(request.POST, request.FILES)

    elif post_type == 'dog':
        form = AddDogForm(request.POST, request.FILES)

    else:
        form = AddOtherForm(request.POST, request.FILES,
                            initial={Posts.animal_type.field.name: 3})

    template_name = 'posts/add_post.html'
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        cleaned_data = form.cleaned_data

        if post_type == 'cat':
            cleaned_data['animal_type'] = 1
        elif post_type == 'dog':
            cleaned_data['animal_type'] = 2
        else:
            cleaned_data['animal_type'] = 3
        new_post = Posts.objects.create(
            user=request.user,
            **cleaned_data
        )
        new_post.save()
        messages.success(request, 'Ваш пост был успешно создан')
        return redirect('users:profile')
    return render(request, template_name, context)


def edit_post(request, pk):
    curr_post = get_object_or_404(Posts, pk=pk)
    if curr_post.animal_type == 1:
        form = AddCatForm(
            data=request.POST,
            files=request.FILES,
            instance=curr_post
        )
    elif curr_post.animal_type == 2:
        form = AddDogForm(
            data=request.POST,
            files=request.FILES,
            instance=curr_post
        )
    else:
        form = AddOtherForm(
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
