from django import forms
from django.forms import fields

from .models import Tag, Post



class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag
        fields = ('__all__')


class PostForm(forms.ModelForm):
    
    class Meta: 
        model = Post
        fields = ('name', 'article', 'tags')
    




