# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billit', '0009_auto_20170118_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='bulk_import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='prod_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
