from django.contrib import admin
from .models import Publisher, Article


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher')


# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Article, ArticleAdmin)
