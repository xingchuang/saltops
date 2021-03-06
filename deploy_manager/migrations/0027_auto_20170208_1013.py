# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0026_projectversion_sub_job_script_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='job_script_type',
            field=models.IntegerField(choices=[(0, 'sls'), (1, 'shell'), (100, '----')], default=0, verbose_name='脚本语言'),
        ),
        migrations.AlterField(
            model_name='projectversion',
            name='sub_job_script_type',
            field=models.IntegerField(choices=[(0, 'sls'), (1, 'shell'), (100, '----')], default=100, verbose_name='脚本语言'),
        ),
    ]
