from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

LOG_IN_URL = reverse('guitar-lovers-login')

REGISTRATION_URL = reverse('guitar-lovers-register')

USER_PAYLOAD = {'username': 'testman',
                'email': 'testman@mansmail.com',
                'password1': 'test123123',
                'password2': 'test123123'
                }


class ProfileTestCase(TestCase):
    """Below we write all the tests related to Profile model"""

    def setUp(self):
        """Setting up common variables for the test"""
        self.client = Client()
        self.user = User.objects.create_user(username='testUser',
                                             email='testmail@mail.com',
                                             password='test123123')

    def test_user_registration(self):
        """Test that user registration works"""
        res = self.client.post(REGISTRATION_URL, USER_PAYLOAD)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, '/login/')

    def test_log_in_works(self):
        """Test that the the log in function works"""
        res = self.client.post(LOG_IN_URL, {'username': 'testUser',
                                            'password': 'test123123'})
        self.assertEqual(res.status_code, status.HTTP_302_FOUND)
        self.assertEqual(res.url, '/')
