# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150706_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='IT_AS_LIFE',
            field=models.IntegerField(default=0, verbose_name='\u6280\u672for\u968f\u7b14', choices=[(0, 'IT\u6280\u672f'), (1, '\u751f\u6d3b\u968f\u7b14')]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u540d\u79f0'),
        ),
    ]
