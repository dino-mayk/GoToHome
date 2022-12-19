from django.test import TestCase

from users.models import CustomUser


class CustomUserTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = CustomUser.objects.create(
            email='test@gmail.com',
            password='123.,Abasd',
        )

    def tear_down():
        CustomUser.objects.delete()
        super().tearDown()

    def test_count_users(self):
        users_count = CustomUser.objects.count()
        self.assertEqual(CustomUser.objects.count(), users_count)
