# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0008_auto_20170121_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployjob',
            name='deploy_status',
            field=models.IntegerField(blank=True, choices=[(0, '\u90e8\u7f72\u4e2d'), (1, '\u90e8\u7f72\u5b8c\u6210'), (2, '\u90e8\u7f72\u5931\u8d25')], default=0, max_length=255, verbose_name='\u90e8\u7f72\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='projectversion',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='doc/script/files', verbose_name='\u7248\u672c'),
        ),
    ]
