# -*- coding:utf-8 -*-
import logging

from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView, ArchiveIndexView, FormView

from blog.form import ContactForm
from .models import Category, Tag, Article
from webblog.settings import DEFAULT_FROM_EMAIL
logger = logging.getLogger(__name__)


class BaseMixin(object):
    """BaseMixin是最基本的视图类，所有类都通过继承BaseMixin类来加载生成的侧边栏数据"""

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            context['recently_article'] = Article.objects.values('title', 'en_title').filter(status=0).order_by(
                '-create_time')[:10]
            context['tag_cloud_list'] = Tag.objects.values('name', 'en_name').filter(status=0)
            context['category_list'] = Category.objects.prefetch_related('article_set').filter(status=0)
        except Exception as e:
            logger.error(u'[BaseMixin]加载出错')

        return context


class IndexView(BaseMixin, ListView):
    """IndexView就是所谓的主页，通过继承BaseMixin和ListView通用视图来加载侧边栏数据和生成文章列表"""
    context_object_name = 'article_list'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        article_list = Article.objects.select_related('category').filter(status=0, IT_AS_LIFE=0)
        return article_list

class LifeView(BaseMixin, ListView):
    """生活随笔栏目"""
    context_object_name = 'article_list'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        article_list = Article.objects.select_related('category').filter(status=0, IT_AS_LIFE=1)
        return article_list


class CategoryView(BaseMixin, ListView):
    """CategoryView是查询属于该分类下的文章，加载侧边栏数据，生成属于该分类的文章列表"""
    context_object_name = 'article_list'
    template_name = 'category.html'
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs.get('category', )
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
    """TagView是查询属于该标签下的文章，加载侧边栏数据，生成属于该标签的文章列表"""
    context_object_name = 'article_list'
    template_name = 'tag.html'
    paginate_by = 10

    def get_queryset(self):
        self.tag = self.kwargs.get('tag', )
        article_list = Article.objects.select_related('category').filter(tag__en_name=self.tag)
        return article_list

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['title'] = self.tag + ' |'
        return context


class SearchView(BaseMixin, ListView):
    """SearchView是搜索视图，通过前端获取来的关键字来对文章的标题，
    内容和摘要进行查找，返回匹配到的文章列表，并加载侧边栏数据"""
    context_object_name = 'article_list'
    template_name = 'search.html'
    paginate_by = 10

    def get_queryset(self):
        self.s = self.request.GET.get('s', )
        if self.s:
            qset = (Q(title__icontains=self.s) | Q(content__icontains=self.s) | Q(summary__icontains=self.s))
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
    """ArticleDetailView是查看详细文章的视图，只能返回一个对象，加载侧边栏数据"""
    queryset = Article.objects.filter(status=0)
    context_object_name = 'article'
    template_name = 'detail.html'
    slug_field = 'en_title'

    def get_object(self, queryset=None):
        self.object = super(ArticleDetailView, self).get_object()
        self.object.view_time += 1
        self.object.last_accessed = timezone.now()
        self.object.save(update_fields=['view_time', 'last_accessed'])
        return self.object

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        pre_article_id = self.object.id + 1
        next_article_id = self.object.id - 1
        try:
            pre_article = Article.objects.get(id=pre_article_id)
        except Article.DoesNotExist:
            pre_article = None

        try:
            next_article = Article.objects.get(id=next_article_id)
        except Article.DoesNotExist:
            next_article = None

        context['pre_article'] = pre_article
        context['next_article'] = next_article
        context['title'] = self.object.en_title + ' |'
        return context


class ArchiveView(BaseMixin, ArchiveIndexView):
    """ArchiveView是所有文章的归档总结，加载侧边栏数据"""
    model = Article
    context_object_name = 'archive_list'
    template_name = 'archive.html'
    date_field = 'pub_time'

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        context['title'] = 'Archive' + ' |'
        return context


class ContactView(FormView):
    """ContactView是一个发送反馈信息的表单视图"""
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        user_name = form.cleaned_data['name']
        user_subject = form.cleaned_data['subject']
        user_email = form.cleaned_data['email']
        user_message = form.cleaned_data['message']
        send_subject = u'河图洛书'
        send_message = u'- - 您的建议已经收到，Thankyou very very much - -'
        user_message = user_message + '\n' + 'username: %s \nfrom email: %s' % (user_name, user_email)
        try:
            send_mail(send_subject, send_message, DEFAULT_FROM_EMAIL, [user_email])
            send_mail(user_subject, user_message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
        except BadHeaderError:
            return HttpResponse('Invaild header fount.')

        return super(ContactView, self).form_valid(form)
