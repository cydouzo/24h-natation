# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20170204_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activites',
            field=models.ManyToManyField(blank=True, null=True, to='event.Activity'),
        ),
        migrations.AlterField(
            model_name='user',
            name='binets',
            field=models.ManyToManyField(blank=True, null=True, to='event.Binet'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]