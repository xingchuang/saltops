# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0016_auto_20170128_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodule',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmodule',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='job_script_type',
            field=models.IntegerField(choices=[(0, 'sls'), (1, 'shell')], default=0, verbose_name='脚本语言'),
        ),
    ]