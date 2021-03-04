from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, default="", related_name="Posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title
