# -*- coding:utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, ArchiveIndexView
from .models import Category, Tag, Article
import logging
logger = logging.getLogger(__name__)


class BaseMixin(object):

    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)

        try:
            context['recently_article'] = Article.objects.filter(status=0).order_by('-create_time')[:10]
            context['tag_cloud_list'] = Tag.objects.filter(status=0)
            context['category_list'] = Category.objects.filter(status=0)
        except Exception as e:
            logger.error(u'[BaseMixin]加载出错')

        return context


class IndexView(BaseMixin, ListView):
    context_object_name = 'article_list'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        article_list = Article.objects.filter(status=0)
        return article_list


class CategoryView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'category.html'
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs.get('category',)
        try:
            article_list = Category.objects.get(en_name=self.category).article_set.all()
        except Category.DoesNotExist:
            logger.error(u'[CategoryView]此分类不存在:[%s]' % Category)
            raise Http404

        return article_list

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['title'] = self.category + '|'
        return context


class TagView(BaseMixin, ListView):
    pass


class SearchView(BaseMixin, ListView):
    pass


class ArticleDetailView(BaseMixin, DetailView):
    pass