# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResistenciaCoC', '0002_auto_20160123_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='war',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
