from django.contrib import admin

from chat.models import Message


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['username', 'room', 'date_added', ]
