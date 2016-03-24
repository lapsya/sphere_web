# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_shopuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_cart', to='shop.Cart'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='laid_off',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_laid_off_cart', to='shop.Cart'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='orders',
            field=models.ManyToManyField(blank=True, to='shop.Order'),
        ),
    ]
