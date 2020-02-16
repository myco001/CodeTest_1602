from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=16383)
    urlToImage = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publishedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
