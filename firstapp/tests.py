from django.test import TestCase
from django.urls import reverse

from .models import Post, User


class PostPublicTests(TestCase):
    """Here we will  writes tests for views that work for non authenticated
    users"""

    def setUp(self):
        """here we make create some posts so we can use them later"""
        self.user = User.objects.create_user(username='testuser',
                                             email='testmail@email.com',
                                             password='test123123')
        self.post1 = Post.objects.create(title='Test Post', content='some random content',
                                         author=self.user)
        self.post2 = Post.objects.create(title='Test Post2', content='some random content2',
                                         author=self.user)

    def test_post_list_views(self):
        """Tests that the post list view works"""
        res = self.client.get(reverse('guitar-lovers-fourms'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Test Post')
        self.assertTemplateUsed(res, 'firstapp/g-l-fourms.html')
        self.assertContains(res, self.post2.title)

    def test_post_detailed_view(self):
        """Test that post detail view works as expected"""
        res = self.client.get(reverse('post-detail', args=[1]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.post1.title)
        self.assertTemplateUsed(res, 'firstapp/post_detail.html')

    def test_that_post_cant_be_created(self):
        """Test that creating posts while unauthenticated fails"""
        res = self.client.get('forums/new/')
        self.assertEqual(res.status_code, 404)

    def test_that_updating_or_deleting_wont_work(self):
        """Test that updating or deleting posts won't work"""
        res = self.client.get('forums/<int:pk>/update/')
        self.assertEqual(res.status_code, 404)

        res = self.client.get('forums/<int:pk>/delete/')
        self.assertEqual(res.status_code, 404)

    def test_that_user_post_list_works(self):
        """Test that you can access post list by a single
        user without authentication"""
        res = self.client.get(reverse('user-posts', args=[self.user.username]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.post1.title)
        self.assertContains(res, self.post2.title)


class PostPrivateTests(TestCase):
    """Below we write all the tests for post models while authenticated"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             email='testmail@email.com',
                                             password='test123123')
        self.client.force_login(user=self.user)

        self.post1 = Post.objects.create(title='Test Post', content='some random content',
                                         author=self.user)
        self.post2 = Post.objects.create(title='Test Post2', content='some random content2',
                                         author=self.user)

    def test_post_creation(self):
        """Test that authenticated user can make new posts"""
        res = self.client.get(reverse('post-new'))
        self.assertEqual(res.status_code, 200)
        # check if the right template is used
        self.assertTemplateUsed(res, 'firstapp/post_form.html')
        # check if 'title' ic present in the template
        self.assertContains(res, 'title')
        # check if username is not present in the template
        self.assertNotContains(res, 'username')

    def test_detail_view_contain_update_and_delete(self):
        """Test if the user views his own post then he has the option to
        delete the post and edit"""
        res = self.client.get(reverse('post-detail', args=[1]))

        # check if the res returns http_200
        self.assertEqual(res.status_code, 200)
        # check if the right template is used
        self.assertTemplateUsed(res, 'firstapp/post_detail.html')
        # check is the template contains delete
        self.assertContains(res, 'delete')
        # check if the template contains update
        self.assertContains(res, 'update')

    def test_check_if_post_update_works(self):
        """Send updated payload to the view and check if the post is
        being updated"""
        res = self.client.post(reverse('post-update', args=[1]), {'title': 'Test Post',
                                                                  'content': 'some random content',
                                                                  'author': self.user})

        # check if the res is http_302 that is redirect
        self.assertEqual(res.status_code, 302)
        # check if update view uses the right template
        # self.assertTemplateUsed(res, 'firstapp/post_detail.html')

    def test_check_if_post_delete_works(self):
        """Test if post method was used on the delete view it would
        return http_200"""
        res = self.client.post(reverse('post-delete', args=[1]))

        # check if the the res.status_code is 302
        self.assertEqual(res.status_code, 302)
