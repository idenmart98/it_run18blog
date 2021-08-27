from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    tag = models.CharField(max_length=50)
    article = models.TextField()

    tags = models.ManyToManyField(Tag,related_name= 'post', verbose_name = 'Теги')

