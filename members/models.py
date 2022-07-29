
from audioop import reverse
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/",default = 'default.png')
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    followers = models.ManyToManyField('Profile', related_name='myfollowers', blank=True)
    followings = models.ManyToManyField('Profile', related_name='myfollowings', blank=True)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('profile', kwargs = {'username':self.user.username})