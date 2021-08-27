from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100)
    article = models.TextField()
    tags = models.ManyToManyField(Tag,related_name= 'post', verbose_name = 'Теги')

    def __str__(self):
        return self.name

