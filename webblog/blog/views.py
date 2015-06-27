# -*- coding:utf-8 -*-
from django.db.models import Q
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

            context['recently_article'] = Article.objects.values('title', 'en_title').filter(status=0).order_by('-create_time')[:10]
            context['tag_cloud_list'] = Tag.objects.values('name', 'en_name').filter(status=0)


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
        context['title'] = self.category + ' |'
        return context


class TagView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'tag.html'
    paginate_by = 10

    def get_queryset(self):
        self.tag = self.kwargs.get('tag',)
        article_list = Tag.objects.get(en_name=self.tag).article_set.all()
        return article_list

    def get_context_data(self, *args, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['title'] = self.tag + ' |'
        return context


class SearchView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'search.html'
    paginate_by = 10

    def get_queryset(self):
        self.s = self.request.GET.get('s',)
        if self.s:
            article_list = Article.objects.only('title', 'content').filter(Q(title__icontains=self.s)|Q(content__icontains=self.s), status=0)
        else:
            article_list = Article.objects.defer('content').filter(status=0)

        return article_list

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['title'] = self.s + ' |'
        context['s'] = self.s
        return context


class ArticleDetailView(BaseMixin, DetailView):
    pass