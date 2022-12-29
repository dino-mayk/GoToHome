from django.db import models


class PostsManager(models.Manager):
    def homepage(self):
        return (
            self.get_queryset()
                .filter(status=True)
                .select_related('user')
                .order_by('title')
        )

    def dogfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=2,
            **kwargs)

    def catfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=1,
            **kwargs)

    def otherfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=3,
            **kwargs)


class FavManager(models.Manager):
    def get_user_and_post(self, user, post):
        return self.filter(user=user) & self.filter(post=post)

    def get_user_fav_posts(self, user):
        post_ids = set(
            post['post_id'] for post in self.filter(
                user_id=user).values('post_id').distinct()
        )
        return post_ids
