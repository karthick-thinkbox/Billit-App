# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billit', '0007_auto_20170117_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='purchase_price',
            field=models.IntegerField(null=True),
        ),
    ]
