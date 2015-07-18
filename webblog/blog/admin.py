# -*- coding:utf-8 -*-
import datetime

from django.contrib import admin
from django.utils import timezone

from .models import Category, Tag, Article

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'分类信息', {'fields': ['name', 'en_name', 'des', ]}),
        (u'状态信息', {'fields': ['status', 'rank', ]}),
        (u'创建时间', {'fields': ['create_time']}),
    ]

    readonly_fields = ('create_time', )
    list_display = ['name', 'status', 'rank', 'create_time', ]
    list_filter = ['status', 'create_time']
    list_display_links = ['name', ]
    search_fields = ('name', 'en_name', )


class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'标签信息', {'fields': ['name', 'en_name', ]}),
        (u'状态信息', {'fields': ['status', 'rank', ]}),
        (u'创建时间', {'fields': ['create_time']}),
    ]
    readonly_fields = ('create_time', )
    list_display = ['name', 'status', 'rank', 'create_time', ]
    list_filter = ['status', 'create_time']
    list_display_links = ['name', ]
    search_fields = ('name', 'en_name', )


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'文章信息', {'fields': ['author', 'title', 'en_title', 'summary', 'category', 'tag', ]}),
        (u'文章内容', {'fields': ['content', ]}),
        (u'状态信息', {'fields': ['IT_AS_LIFE', 'status', 'not_read', 'rank', ]}),
        (u'发布时间', {'fields': ['pub_time', ]}),
        (u'创建时间', {'fields': ['create_time', 'update_time', ]}),
    ]

    filter_horizontal = ('tag', )
    readonly_fields = ('create_time', 'update_time', )
    list_display = ['title', 'status', 'rank', 'was_published_recently', 'create_time', ]
    list_filter = ['status', 'create_time']
    list_display_links = ['title', ]
    search_fields = ('title', 'en_title', 'summary', )
    save_on_top = True

    def was_published_recently(self, obj):
        return timezone.now() - datetime.timedelta(days=7) <= obj.pub_time <= timezone.now()

    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布?'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
