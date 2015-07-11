# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150707_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name='\u4e66\u540d')),
                ('summary', models.CharField(max_length=150, verbose_name='\u63cf\u8ff0')),
                ('content', models.TextField(verbose_name='\u56fe\u4e66\u51fa\u7248\u4fe1\u606f')),
                ('image', models.ImageField(upload_to=b'photos', verbose_name='\u56fe\u7247')),
                ('rank', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('is_recommend', models.BooleanField(default=0, verbose_name='\u662f\u5426\u63a8\u8350', choices=[(0, '\u63a8\u8350'), (1, '\u4e0d\u63a8\u8350')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['rank'],
                'verbose_name': '\u56fe\u4e66\u63a8\u8350',
                'verbose_name_plural': '\u56fe\u4e66\u63a8\u8350',
            },
        ),
    ]
