# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20160213_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contestant',
            old_name='qsate_array',
            new_name='qstate_array',
        ),
    ]