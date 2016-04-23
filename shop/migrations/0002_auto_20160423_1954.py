# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(null=True, to='shop.Tag'),
        ),
    ]