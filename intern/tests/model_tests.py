# import mock
# from datetime import datetime, timedelta
#
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.template.defaultfilters import slugify
# from django.utils import timezone
#
# from intern.models import Post
#
#
# class PostModelTest(TestCase):
#     """Here we write all the methods for the post model"""
#
#     def setUp(self):
#         """lets create a user object so we can use it can
#         be used for post relation"""
#         self.user = get_user_model().objects.create_user(username='testman',
#                                                          email='testmail@mail.com',
#                                                          password='test123123')
#         self.user.save()
#
#         # lets create a post model object for testing
#         self.post1 = Post.objects.create(user=self.user,
#                                          title='The title',
#                                          content='Nice content',
#                                          snippet='Dude I was greening out so hard',
#                                          thumbnail_image='image/location.jpg',
#                                          )
#         self.post2 = Post.objects.create(user=self.user,
#                                          title='The title2',
#                                          content='Nice content2',
#                                          snippet='Dude I was greening out so hard2',
#                                          thumbnail_image='image/location2.jpg',
#                                          )
#
#     def test_all_model_creation(self):
#         """test that the model is being created as expected"""
#
#         # check if the object post1 is created
#         self.assertEqual(self.post1, Post.objects.get(title='The title'))
#
#         # check if the object's attributes matches
#         self.assertEqual(self.post1.snippet, 'Dude I was greening out so hard')
#
#         # check if the objects contains certain data
#         self.assertEqual(self.post1.content, 'Nice content')
#
#     def test_model_string_representation_func(self):
#         """Test that __str__ method works as expected"""
#         self.assertEqual(str(self.post1), self.post1.title)
#
#     def test_model_publish_method(self):
#         """check the default status and status after publish
#         method call"""
#
#         # check if the default status is false
#         self.assertFalse(self.post1.status)
#
#         # check the status if true after calling the publish method
#         self.post1.publish()
#         self.assertTrue(self.post1.status)
#
#     def test_model_slug(self):
#         """Call the save method and check if the slug is
#         what we expect it to be"""
#
#         # check if the object has right slug
#         self.assertEqual(self.post1.slug, slugify(self.post1.title))
#
#     def test_model_absolute_url(self):
#         """Use the get_absolute_url method nd check if it works as
#         expected"""
#
#         url = self.post1.get_absolute_url()
#         self.assertEqual(url, f'/blog/{slugify(self.post1.title)}')
#
#     def test_model_creation_time(self):
#         """Lets create a new object but now we will use mock
#         and check if the time is what we expect it to be"""
#
#         post3 = Post.objects.create(user=self.user,
#                                     title='The title3',
#                                     content='Nice content3',
#                                     snippet='Dude I was greening out so hard3',
#                                     thumbnail_image='image/location3.jpg',
#                                     )
#         # now lets see if if the model is created now
#         self.assertAlmostEqual(post3.created_at, timezone.now())
#
#     def test_model_edited_at(self):
#         """Test to check if the edited at time is correct"""
#
#         itc_time = datetime.now()
#
#         test_time = itc_time + timedelta(hours=24)
#
#         with mock.patch('django.utils.timezone.now') as mock_now:
#             mock_now.return_value = test_time
#             # print(test_time)
#             self.post1.snippet = 'Edited snippet for time check'
#             self.post1.save()
#
#         # check if the edit time is a day ahead
#         self.assertEqual(self.post1.edited_at.date(),
#                          (self.post1.created_at + timedelta(days=1)).date())
#
#     def test_model_meta_ordering(self):
#         """Test that all the objects of the models are returned
#         in ordered as specified"""
#         # now lets check if the newest object if the first one
#         # in the list. Lets create a post whose time is 1 day ahead of current
#         itc_time = datetime.now()
#
#         test_time = itc_time + timedelta(hours=24)
#
#         # using mock we create a time that is a day ahead of datetime.now()
#         with mock.patch('django.utils.timezone.now') as mock_now:
#             mock_now.return_value = test_time
#             # print(test_time)
#             latest_post = Post.objects.create(user=self.user,
#                                               title='Latest post',
#                                               content='Nice content4',
#                                               snippet='Dude I was greening out so hard4',
#                                               thumbnail_image='image/location4.jpg',
#                                               )
#             latest_post.save()
#
#         object_queryset = Post.objects.all()
#
#         # check if the latest post is first in the list
#         self.assertEqual(object_queryset.first().title, latest_post.title)
