from django.contrib import admin

from .models import Posts, Favourites


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['title', 'user', 'img_tmb', 'animal_type']


admin.site.register(Favourites)
