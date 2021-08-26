from django.db import models
class Blog(models.Model):
    teg = models.CharField(max_length=50)
    article = models.TextField()

