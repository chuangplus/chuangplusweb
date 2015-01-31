# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150128_2133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='images',
            new_name='image',
        ),
        migrations.RenameModel(
            old_name='members',
            new_name='member',
        ),
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
        migrations.RenameModel(
            old_name='projects',
            new_name='project',
        ),
    ]
