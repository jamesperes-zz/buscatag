# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscatag', '0011_auto_20170112_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetolist',
            name='tag',
        ),
        migrations.AddField(
            model_name='projetolist',
            name='tag',
            field=models.ManyToManyField(to='buscatag.Tag'),
        ),
    ]
