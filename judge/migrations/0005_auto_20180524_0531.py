# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_auto_20180523_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
