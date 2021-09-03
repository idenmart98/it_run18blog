from django import forms
from django.forms import fields

from .models import Tag, Post, Comment, PostImage



class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag
        fields = ('__all__')


class PostForm(forms.ModelForm):
    
    class Meta: 
        model = Post
        fields = ('name', 'article', 'tags')

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('name', 'email', 'text', 'post')

class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)    




