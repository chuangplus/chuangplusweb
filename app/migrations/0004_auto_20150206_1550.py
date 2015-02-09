# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150206_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='is_financing',
            new_name='is_roadshowing',
        ),
        migrations.AlterField(
            model_name='project',
            name='link1',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='link2',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='link3',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
