# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def index(request):
    articles_list = Article.objects.all()[::-1]
    page=request.GET.get('page')

    article_images = ArticleImage.objects.filter(is_main=True)
    paginator=Paginator(articles_list,12)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    return render(request,'html/index.html',locals(), {'articles':articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'html/article.html',locals())