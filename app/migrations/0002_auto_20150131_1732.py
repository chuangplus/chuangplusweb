# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_id', models.IntegerField()),
                ('image_path', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=60)),
                ('text', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=250)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_id', models.IntegerField()),
                ('m_name', models.CharField(max_length=30)),
                ('m_head_path', models.CharField(max_length=250)),
                ('m_title', models.CharField(max_length=30)),
                ('introduction', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_id', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField(blank=True)),
                ('link', models.CharField(max_length=250)),
                ('image_path', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('field1', models.CharField(max_length=30)),
                ('field2', models.CharField(max_length=30)),
                ('field3', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('slogan', models.CharField(max_length=120)),
                ('summary', models.TextField(blank=True)),
                ('province', models.CharField(max_length=30)),
                ('stage', models.CharField(max_length=30)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_phone', models.CharField(max_length=30)),
                ('contact_email', models.CharField(max_length=60)),
                ('contact_weixin', models.CharField(max_length=30)),
                ('link1', models.CharField(max_length=250)),
                ('link2', models.CharField(max_length=250)),
                ('link3', models.CharField(max_length=250)),
                ('business_model', models.TextField(blank=True)),
                ('plan', models.TextField(blank=True)),
                ('market_analysis', models.TextField(blank=True)),
                ('check_status', models.IntegerField(default=0)),
                ('finance_status', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='images',
        ),
        migrations.DeleteModel(
            name='members',
        ),
        migrations.DeleteModel(
            name='posts',
        ),
        migrations.DeleteModel(
            name='projects',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='rel_id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_id',
        ),
    ]
