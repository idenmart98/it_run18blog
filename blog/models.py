from django.db import models
from django_quill.fields import QuillField

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    article = QuillField()
    liked = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag,related_name= 'post', verbose_name = 'Теги')

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name= 'comment', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Комментарий был оставлен {self.name} к посту {self.post}'
