from enum import auto
from pyexpat import model
from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    text = models.TextField(max_length = 2000)
    author = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    def __str__(self) -> str:
        return self.title + self.author


class Comment(models.Model):
    blog_id = models.ForeignKey(Blog , on_delete = models.CASCADE)
    comment_text = models.TextField(max_length = 700)
    date = models.DateTimeField(auto_now_add=True)
