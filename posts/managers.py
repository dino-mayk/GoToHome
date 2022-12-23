from django.db import models


class PostsManager(models.Manager):
    def homepage(self):
        return (
            self.get_queryset()
                .filter(status=True)
                .select_related('user')
                .order_by('title')
        )


class FavManager(models.Manager):
    def get_user_and_post(self, user, post):
        return self.filter(user=user) & self.filter(post=post)

    def get_user_fav_posts(self, user):
        post_ids = set(
            post['post_id'] for post in self.filter(
                user_id=user).values('post_id').distinct()
        )
        return post_ids
