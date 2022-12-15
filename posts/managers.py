from django.db import models


class PostsManager(models.Manager):
    def homepage(self):
        return (
            self.get_queryset()
                .select_related('user')
                .order_by('title')
        )
