from django.contrib import admin

from .models import Posts

@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['name', 'user', 'img_tmb']
