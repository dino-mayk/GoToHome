from django.contrib.auth.models import UserManager


class UserManager(UserManager):
    def active(self):
        return (
            self.get_queryset()
                .filter(is_active=True)
                .order_by('username')
        )
