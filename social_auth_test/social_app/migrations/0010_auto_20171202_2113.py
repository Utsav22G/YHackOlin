# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0009_auto_20171202_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorite_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='helpful_links',
        ),
        migrations.RemoveField(
            model_name='post',
            name='material_ls',
        ),
        migrations.RemoveField(
            model_name='post',
            name='personal_links',
        ),
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='vote_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(null=True, to='social_app.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='experiences',
            field=models.ManyToManyField(null=True, to='social_app.Experience'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pictures',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]