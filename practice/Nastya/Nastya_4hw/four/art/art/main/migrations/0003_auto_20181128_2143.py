# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181128_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arts',
            name='link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
