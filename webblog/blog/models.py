# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import markdown2
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

STATUS = (
    (0, u'正常'),
    (1, u'删除'),
    (2, u'草稿'),
)

LIFE = (
    (0, u'IT技术'),
    (1, u'生活随笔'),
)


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'名称')
    en_name = models.CharField(max_length=40, verbose_name=u'英文名称')
    des = models.CharField(max_length=100, verbose_name=u'分类描述')
    status = models.IntegerField(default=0, choices=STATUS, verbose_name=u'状态')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'分类管理'
        ordering = ['rank', '-create_time', ]


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    en_name = models.CharField(max_length=40, verbose_name=u'英文名称')
    status = models.IntegerField(default=0, choices=STATUS, verbose_name=u'状态')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'标签管理'
        ordering = ['rank', '-create_time', ]


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name=u'作者')
    title = models.CharField(max_length=40, verbose_name=u'标题')
    en_title = models.CharField(max_length=40, verbose_name=u'英文标题')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'内容')
    content_html = models.TextField(editable=False, blank=True, null=True)
    view_time = models.IntegerField(editable=False, default=0, verbose_name=u'访问次数')
    last_accessed = models.DateTimeField(editable=False, blank=True, null=True, verbose_name=u'最近访问时间')
    IT_AS_LIFE = models.IntegerField(default=0, choices=LIFE, verbose_name=u'技术or随笔')
    status = models.IntegerField(default=0, choices=STATUS, verbose_name=u'状态')
    not_read = models.BooleanField(default=0, verbose_name=u'禁止阅读')
    rank = models.IntegerField(default=0, verbose_name=u'排序')

    pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content_html = markdown2.markdown(self.content, extras=['fenced-code-blocks']).encode('utf-8')
        super(Article, self).save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'文章管理'
        ordering = ['rank', '-create_time', ]


class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name=u'书名')
    en_title = models.CharField(max_length=30, null=True, verbose_name=u'英文标记')
    summary = models.TextField(max_length=150, verbose_name=u'描述')
    content = models.TextField(verbose_name=u'图书出版信息')
    image = models.ImageField(upload_to='photos', verbose_name=u'原图')
    image_140x180 = ImageSpecField(
        source='image', processors=[ResizeToFill(140, 180)],
        format='JPEG', options={'quality': 95})
    image_300x360 = ImageSpecField(
        source='image', processors=[ResizeToFill(300, 360)],
        format='JPEG', options={'quality': 95})

    rank = models.IntegerField(default=0, verbose_name=u'排序')
    is_recommend = models.BooleanField(default=0, verbose_name=u'是否推荐')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['rank']
        verbose_name_plural = verbose_name = u'图书推荐'



