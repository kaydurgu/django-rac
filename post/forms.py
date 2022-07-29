from django import forms
from .models import Project


class AdvertismentForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']


