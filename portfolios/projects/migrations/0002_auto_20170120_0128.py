# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='future_job',
            field=models.CharField(max_length=40),
        ),
    ]
