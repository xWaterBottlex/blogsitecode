from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import reverse as api_reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def owner(self):
        return self.user

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_api_url(self):
        return api_reverse("post-api:post-rud", kwargs=[self.pk])
