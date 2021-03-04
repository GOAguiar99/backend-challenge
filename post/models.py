from django.db import models
from django.contrib.auth.models import User
from topic.models import Topic
from django.urls import reverse


class Post(models.Model):
    topic = models.ForeignKey(Topic, default="", related_name="Topics", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})




