# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='nothing', max_length=100),
            preserve_default=False,
        ),
    ]
