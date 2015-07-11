# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150711_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='en_title',
            field=models.CharField(max_length=30, null=True, verbose_name='\u82f1\u6587\u6807\u8bb0'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=150, verbose_name='\u63cf\u8ff0'),
        ),
    ]
