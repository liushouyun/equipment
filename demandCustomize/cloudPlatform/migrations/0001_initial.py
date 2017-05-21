# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisTool',
            fields=[
                ('AnalysisToolID', models.AutoField(primary_key=True, serialize=False)),
                ('AnalysisToolName', models.CharField(max_length=45)),
                ('AnalysisToolDescrip', models.CharField(blank=True, max_length=100)),
                ('AnalysisToolPlatform', models.CharField(max_length=15)),
                ('AnalysisToolVersion', models.CharField(max_length=10)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisTool_has_Tag',
            fields=[
                ('AnalysisToolID_TagID', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('AnalysisTool_AnalysisToolID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.AnalysisTool')),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisToolConnect',
            fields=[
                ('DemandTemplateID_FrontID_BackID', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('DataDescrip', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisToolType',
            fields=[
                ('AnalysisToolTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('AnalysisToolTypeName', models.CharField(max_length=45)),
                ('AnalysisToolTypeDescrip', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('DemandID', models.AutoField(primary_key=True, serialize=False)),
                ('DemandName', models.CharField(max_length=45)),
                ('DemandDescrip', models.CharField(blank=True, max_length=100)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demand_has_Tag',
            fields=[
                ('DemandID_TagID', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('Demand_DemandID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.Demand')),
            ],
        ),
        migrations.CreateModel(
            name='DemandTemplate',
            fields=[
                ('DemandTemplateID', models.AutoField(primary_key=True, serialize=False)),
                ('DemandTemplateName', models.CharField(max_length=45)),
                ('DemandTemplateDescrip', models.CharField(blank=True, max_length=100)),
                ('StartMethodNode', models.IntegerField(default=0)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
                ('DemandTemplatePara', models.CharField(max_length=500)),
                ('Demand_DemandID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.Demand')),
            ],
        ),
        migrations.CreateModel(
            name='DemandTemplateNode',
            fields=[
                ('DemandTemplateNodeID', models.AutoField(primary_key=True, serialize=False)),
                ('NodeType', models.CharField(max_length=15)),
                ('AnalysisToolPara', models.CharField(blank=True, max_length=500)),
                ('AnalysisTool_AnalysisToolID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.AnalysisTool')),
                ('DemandTemplate_DemandTemplateID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.DemandTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='DemandType',
            fields=[
                ('DemandTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('DemandTypeName', models.CharField(max_length=45)),
                ('DemandTypeDescrip', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('ResultFileID', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('ResultFileName', models.CharField(max_length=45)),
                ('ResultFileUrl', models.CharField(max_length=100)),
                ('ResultFileType', models.CharField(max_length=15)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('TagID', models.AutoField(primary_key=True, serialize=False)),
                ('TagLabel', models.CharField(max_length=45)),
                ('TagDescrip', models.CharField(blank=True, max_length=100)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('TagTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('TagTypeName', models.CharField(max_length=45)),
                ('TagTypeDescrip', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationDraw',
            fields=[
                ('VisualizationDraw_RecordID', models.AutoField(primary_key=True, serialize=False)),
                ('VisualizationFigureID', models.IntegerField()),
                ('ResultFile_ResultID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.ResultFile')),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationDrawInfo',
            fields=[
                ('VisualizationDrawID', models.AutoField(primary_key=True, serialize=False)),
                ('VisualizationDrawName', models.CharField(max_length=45)),
                ('VisualizationDrawDescrip', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationTool',
            fields=[
                ('VisualizationToolID', models.AutoField(primary_key=True, serialize=False)),
                ('VisualizationToolName', models.CharField(max_length=45)),
                ('VisualizationToolDescrip', models.CharField(max_length=100)),
                ('VisualizationToolVersion', models.CharField(max_length=10)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationTool_has_Tag',
            fields=[
                ('VisualizationToolID_TagID', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('Tag_TagID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.Tag')),
                ('VisualizationTool_VisualizationToolID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.VisualizationTool')),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationToolType',
            fields=[
                ('VisualizationToolTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('VisualizationToolTypeName', models.CharField(max_length=45)),
                ('VisualizationToolTypeDescrip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='visualizationtool',
            name='VisualizationToolType_VisualizationToolID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.VisualizationToolType'),
        ),
        migrations.AddField(
            model_name='visualizationdraw',
            name='VisualizationDrawID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudPlatform.VisualizationDrawInfo'),
        ),
        migrations.AddField(
            model_name='visualizationdraw',
            name='VisualizationTool_VisualizationToolID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.VisualizationTool'),
        ),
        migrations.AddField(
            model_name='tag',
            name='TagType_TagTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.TagType'),
        ),
        migrations.AddField(
            model_name='demand_has_tag',
            name='Tag_TagID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.Tag'),
        ),
        migrations.AddField(
            model_name='demand',
            name='DemandType_DemandTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.DemandType'),
        ),
        migrations.AddField(
            model_name='analysistoolconnect',
            name='BackNodeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BackDemandTemplateNode', to='cloudPlatform.DemandTemplateNode'),
        ),
        migrations.AddField(
            model_name='analysistoolconnect',
            name='DemandTemplate_DemandTemplateID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudPlatform.DemandTemplate'),
        ),
        migrations.AddField(
            model_name='analysistoolconnect',
            name='FrontNodeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FrontDemandTemplateNode', to='cloudPlatform.DemandTemplateNode'),
        ),
        migrations.AddField(
            model_name='analysistool_has_tag',
            name='Tag_TagID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.Tag'),
        ),
        migrations.AddField(
            model_name='analysistool',
            name='AnalysisToolType_AnalysisToolTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cloudPlatform.AnalysisToolType'),
        ),
    ]
