# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscatag', '0004_projetolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='slack',
            field=models.CharField(default=111111, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tel',
            field=models.IntegerField(default=11111),
            preserve_default=False,
        ),
    ]
