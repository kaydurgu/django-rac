
from django.db import models

class CustomerMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email
    class Meta:
        ordering = ['-id']  
