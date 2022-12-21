from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'сообщение от пользователя {self.username}'

    class Meta:
        ordering = ('date_added', )
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
