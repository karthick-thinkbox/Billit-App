# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billit', '0010_auto_20170118_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulk_import',
            name='file_name',
            field=models.FileField(upload_to='/data'),
        ),
    ]
