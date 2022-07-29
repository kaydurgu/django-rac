
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Profile

class Register(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled = True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = Profile
        fields = ['username','first_name','last_name', 'bio','facebook','twitter','instagram','profile_pic']
