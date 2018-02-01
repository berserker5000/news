# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]
    inlines = [ArticleImageInline]

    class Meta:
        model = Article

class ArticleImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArticleImage._meta.fields]

    class Meta:
        model = ArticleImage


admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)