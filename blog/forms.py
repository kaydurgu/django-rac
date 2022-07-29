
from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Comment, Blog


class CommentForm(forms.Form):
    comment_text = forms.CharField(label = '',
    widget=forms.Textarea(attrs={
        'rows':5,
        'cols' : 80,
        'class':'form-control',
        'placeholder': "Напишите коментарий",
        },))
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title'
                }),
            'text': forms.Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Text'
                }),
        }
        labels = {
            'title': '',
            'text': '',
            'cat':'Category',
        }