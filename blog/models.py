from audioop import reverse
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect

class Category(models.Model):
    category = models.CharField(max_length=200 ,unique=True)

    def __str__(self) -> str:
        return self.category
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
class Blog(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    text = models.TextField(max_length = 2000)
    date = models.DateTimeField(auto_now_add = True)
    cat = models.ManyToManyField(Category, blank=False)
    likes = models.ManyToManyField(User, related_name='my_likes' ,blank=True)
    dislikes = models.ManyToManyField(User,related_name='my_dislikes', blank=True)
    saved = models.ManyToManyField(User , related_name='saved',blank=True)


    def __str__(self) -> str:
        return self.title + ' ' + self.author.username 

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog , on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField(max_length = 700)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username + ' ' + self.blog_id.title 


