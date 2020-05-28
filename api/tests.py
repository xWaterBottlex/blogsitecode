from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from firstapp.models import Post

User = get_user_model()


class PostAPITestCase(APITestCase):
    def setUp(self):
        # user = User(username='testuser', email='testmail@test.com')
        # is also a valid medthod
        user = User.objects.create(username='testuser',
                                   email='testmail@test.com')
        user.set_password('test123')
        user.save()
        post = Post.objects.create(title='some',
                                   content='some content',
                                   author=user)

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)


