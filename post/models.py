from turtle import title
from django.db import models
import datetime

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'post/image')
    url = models.URLField(blank = True)
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title