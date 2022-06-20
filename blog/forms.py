from django import forms
from .models import Comment
class CommentForm(forms.Form):
    comment_text = forms.CharField(label = '',
    widget=forms.Textarea(attrs={
        'rows':5,
        'cols' : 80,
        'class':'form-control',
        'placeholder': "Напишите коментарий",
        },))