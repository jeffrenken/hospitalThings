# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchDemo', '0005_auto_20180128_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
