from django.test import TestCase
from django.urls import reverse, resolve

from intern.views import contact


class PublicEmailTest(TestCase):
    """Testing email for non authenticated users"""

    def test_that_he_right_function_is_used(self):
        """Using resolve test the function"""
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_contact_me_page(self):
        """Test that contact me page is available for non
        authenticated user"""
        res = self.client.get('/contact/')
        # check that the right template is being used
        self.assertTemplateUsed(res, 'intern/contact.html')

        # check that the right content present in the template
        self.assertContains(res, 'Get In Touch')

    def test_view_get_method(self):
        """Test that view is accepting the post method"""
        res = self.client.get(reverse('contact'))

        # now lets check if the values are received
        self.assertEqual(res.status_code, 200)

    def test_mail(self):
        """Test that the send_mail is working"""
        res = self.client.post(reverse('contact'),
                               {'message': 'yo yo yo',
                                'sender_email': ['testmail@mailman.com']})
        self.assertEqual(res.status_code, 200)
