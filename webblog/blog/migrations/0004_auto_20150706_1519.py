# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_content_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_accessed',
            field=models.DateTimeField(verbose_name='\u6700\u8fd1\u8bbf\u95ee\u65f6\u95f4', null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='view_time',
            field=models.IntegerField(default=0, verbose_name='\u8bbf\u95ee\u6b21\u6570', editable=False),
        ),
    ]
