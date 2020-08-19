from django.test import TestCase
from django.core import mail


class EmailModuleTests(TestCase):

    def test_send_mail_works_as_expected(self):
        """Testing with send_mail function mocked at always true"""
        res = mail.send_mail(message='yo yo yo',
                             subject='testing',
                             from_email='gouthambolt@gmail.com',
                             recipient_list=['gouthambolt@outlook.com'])
        self.assertEqual(res, 1)

        # also test that the outbox has sent the mail
        self.assertEqual(len(mail.outbox), 1)
