# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_id',
        ),
        migrations.RemoveField(
            model_name='members',
            name='member_id',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='pro_id',
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
