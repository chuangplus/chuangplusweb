# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='check_status',
            new_name='is_checked',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='finance_status',
            new_name='is_financing',
        ),
    ]
