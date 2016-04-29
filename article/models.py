from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=True , null=True)
  
class ArticlePostAdmin(admin.ModelAdmin):
     list_display = ('title','date_time')

admin.site.register(Article,ArticlePostAdmin)