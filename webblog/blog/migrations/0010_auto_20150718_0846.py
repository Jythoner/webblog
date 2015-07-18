# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150714_1635'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
