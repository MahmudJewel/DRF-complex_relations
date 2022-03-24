from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    desc = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)