# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150206_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='field2',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='field3',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
