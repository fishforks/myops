# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0007_auto_20180516_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deploy',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='deploy',
            name='assigned_to',
        ),
        migrations.DeleteModel(
            name='Deploy',
        ),
    ]