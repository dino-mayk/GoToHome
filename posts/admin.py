from django.contrib import admin

from posts.models import Favourites, Posts, PostsGallery


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'img_tmb',
        'animal_type',
    ]


@admin.register(PostsGallery)
class AdminPostsGallery(admin.ModelAdmin):
    list_display = [
        'item',
        'img_tmb',
    ]


admin.site.register(Favourites)
