# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0013_auto_20171203_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='members',
            field=models.TextField(blank=True, default='Utsav, Emma'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pictures',
            field=models.TextField(blank=True, default='/social_app/img/blank.gif', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.TextField(blank=True, default='Describe your awesome project!'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Project Title', max_length=200),
        ),
    ]