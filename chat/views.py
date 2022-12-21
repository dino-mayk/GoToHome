from django.shortcuts import render

from chat.models import Message


def room(request, room_name):
    messages = Message.objects.filter(room=room_name)[0:25]

    context = {
        'room_name': room_name,
        'messages': messages,
    }

    return render(request, "chat/room.html", context)
