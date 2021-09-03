from django import forms
from django.forms import fields
from django_quill.forms import QuillFormField

from .models import Tag, Post, Comment



class TagForm(forms.ModelForm):
    class Meta: 
        model = Tag
        fields = ('__all__')


class PostForm(forms.ModelForm):
    article = QuillFormField()
    class Meta: 
        model = Post
        fields = ('name', 'article', 'tags', 'image')

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('name', 'email', 'text', 'post')

  




