
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'post/image')
    url = models.URLField(blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['-id']