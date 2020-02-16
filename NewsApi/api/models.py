from django.db import models
from tastypie.resources import ModelResource
from news.models import Article, Publisher


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'articles'


class PublisherResource(ModelResource):
    class Meta:
        queryset = Publisher.objects.all()
        resource_name = 'publishers'
