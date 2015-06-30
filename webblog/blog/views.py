# -*- coding:utf-8 -*-
from django.db.models import Q, F
from django.http import Http404
from django.views.generic import ListView, DetailView, ArchiveIndexView
from .models import Category, Tag, Article
import logging
logger = logging.getLogger(__name__)


class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            context['recently_article'] = Article.objects.values('title', 'en_title').filter(status=0).order_by('-create_time')[:10]
            context['tag_cloud_list'] = Tag.objects.values('name', 'en_name').filter(status=0)
            context['category_list'] = Category.objects.prefetch_related('article_set').filter(status=0)
        except Exception as e:
            logger.error(u'[BaseMixin]加载出错')

        return context


class IndexView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        article_list = Article.objects.select_related('category').filter(status=0)
        return article_list


class CategoryView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'category.html'
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs.get('category',)
        try:
            article_list = Category.objects.prefetch_related('article_set').get(en_name=self.category).article_set.all()
        except Category.DoesNotExist:
            logger.error(u'[CategoryView]此分类不存在:[%s]' % Category)
            raise Http404

        return article_list

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['title'] = self.category + ' |'
        return context


class TagView(BaseMixin, ListView):

    context_object_name = 'article_list'
    template_name = 'tag.html'
    paginate_by = 10

    def get_queryset(self):
        self.tag = self.kwargs.get('tag',)
        article_list = Article.objects.select_related('category').filter(tag__en_name=self.tag)
        return article_list

    def get_context_data(self, **kwargs):
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
            qset = (Q(title__icontains=self.s)|Q(content__icontains=self.s)|Q(summary__icontains=self.s))
            article_list = Article.objects.select_related('category').filter(qset, status=0)
        else:
            article_list = Article.objects.defer('content').filter(status=0)

        return article_list

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['title'] = self.s + ' |'
        context['s'] = self.s
        return context


class ArticleDetailView(BaseMixin, DetailView):

    queryset = Article.objects.filter(status=0)
    context_object_name = 'article'
    template_name = 'detail.html'
    slug_field = 'en_title'

    def get(self, request, *args, **kwargs):
        self.en_title = self.kwargs.get('slug',)
        self.article = self.queryset.prefetch_related('tag').get(en_title=self.en_title)
        self.queryset.update(view_time=F('view_time')+1)
        return super(ArticleDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        pre_article_id = self.article.id + 1
        next_article_id = self.article.id - 1
        try:
            pre_article = Article.objects.get(id=pre_article_id)
        except Article.DoesNotExist:
            pre_article = None

        try:
            next_article = Article.objects.get(id=next_article_id)
        except Article.DoesNotExist:
            next_article = None

        context['pre_article'] = pre_article
        context['next_article']= next_article
        context['title'] = self.en_title + ' |'
        return context

