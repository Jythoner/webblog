# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150711_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='not_read',
            field=models.BooleanField(default=0, verbose_name='\u7981\u6b62\u9605\u8bfb'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_accessed',
            field=models.DateTimeField(verbose_name='\u6700\u8fd1\u8bbf\u95ee\u65f6\u95f4', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_recommend',
            field=models.BooleanField(default=1, verbose_name='\u662f\u5426\u63a8\u8350', choices=[(1, '\u63a8\u8350'), (0, '\u4e0d\u63a8\u8350')]),
        ),
    ]
