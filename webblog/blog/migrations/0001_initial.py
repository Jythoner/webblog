# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u6807\u9898')),
                ('en_title', models.CharField(max_length=40, verbose_name='\u82f1\u6587\u6807\u9898')),
                ('summary', models.TextField(verbose_name='\u6458\u8981')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('view_time', models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u6b21\u6570')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u5220\u9664'), (2, '\u8349\u7a3f')])),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '\u6587\u7ae0\u7ba1\u7406',
                'verbose_name_plural': '\u6587\u7ae0\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('en_name', models.CharField(max_length=40, verbose_name='\u82f1\u6587\u540d\u79f0')),
                ('des', models.CharField(max_length=100, verbose_name='\u5206\u7c7b\u63cf\u8ff0')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u5220\u9664'), (2, '\u8349\u7a3f')])),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '\u5206\u7c7b\u7ba1\u7406',
                'verbose_name_plural': '\u5206\u7c7b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('en_name', models.CharField(max_length=40, verbose_name='\u82f1\u6587\u540d\u79f0')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38'), (1, '\u5220\u9664'), (2, '\u8349\u7a3f')])),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '\u6807\u7b7e\u7ba1\u7406',
                'verbose_name_plural': '\u6807\u7b7e\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categoty',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
