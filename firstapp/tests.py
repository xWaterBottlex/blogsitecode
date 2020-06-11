from django.test import TestCase
from django.urls import reverse

from .models import Post



class PostPublicTests(TestCase):
    """Here we will  writes tests for views that work for non authenticated
    users"""

    def setup(self):
        """here we make create some posts so we can use them later"""
        post = Post.objects.create(title='Test Post', content='some rendom content',
                                   author='superman')
        print(post)                           

    def test_post_list_views(self):
        """Tests that the post list view works"""
        res = self.client.get(reverse('guitar-lovers-fourms'))

