# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20180515_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploydcos',
            name='result',
            field=models.TextField(default='\u7a7a', verbose_name='\u6784\u5efa\u7ed3\u679c'),
        ),
    ]
