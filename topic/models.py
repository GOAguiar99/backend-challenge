from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse("topic:detail", kwargs={"slug": self.slug})
