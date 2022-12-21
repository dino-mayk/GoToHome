from django.contrib import admin

from chat.models import Message


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = [
        'username',
        'room',
        'content',
        'date_added',
    ]
