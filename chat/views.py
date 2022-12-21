from django.shortcuts import redirect, render

from chat.models import Message


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('homepage:home')

    username = request.user.username
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(
        request, 'chat/room.html', {
            'room_name': room_name,
            'username': username,
            'messages': messages
        }
    )
