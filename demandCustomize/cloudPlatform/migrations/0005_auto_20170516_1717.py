# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPlatform', '0004_auto_20170516_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visualizationtooltype',
            old_name='VisualizationToolDescrip',
            new_name='VisualizationToolTypeDescrip',
        ),
        migrations.RenameField(
            model_name='visualizationtooltype',
            old_name='VisualizationToolID',
            new_name='VisualizationToolTypeID',
        ),
        migrations.RenameField(
            model_name='visualizationtooltype',
            old_name='VisualizationToolName',
            new_name='VisualizationToolTypeName',
        ),
    ]
