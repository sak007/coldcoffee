# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbncc', '0003_auto_20170216_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='source_author',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b')], default='a', max_length=100),
            preserve_default=False,
        ),
    ]
