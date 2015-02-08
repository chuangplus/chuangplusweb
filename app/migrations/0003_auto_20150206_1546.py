# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150206_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_checked',
            field=models.CharField(default=b'\xe6\xad\xa3\xe5\x9c\xa8\xe5\xae\xa1\xe6\xa0\xb8\xe4\xb8\xad', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='is_financing',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe8\xb7\xaf\xe6\xbc\x94', max_length=30),
            preserve_default=True,
        ),
    ]
