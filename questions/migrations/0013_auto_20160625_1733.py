# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-25 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_remove_contestant_qstate_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='current_que_id',
            field=models.IntegerField(default=1),
        ),
    ]