# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.db import models
#TODO: https://www.berlingskemedia.dk/
# Create your models here.

class Article(models.Model):
    article_title=models.CharField(max_length=128, default=None,blank=True,null=True)
    short_article=models.TextField(max_length=512, default=None,blank=True,null=True)
    full_article=models.TextField(max_length=999999999, default=None,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" %self.article_title

class ArticleImage(models.Model):
    article=models.ForeignKey(Article,blank=True, null=True, default=None)
    image = models.ImageField(upload_to='pictures')
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" %self.id