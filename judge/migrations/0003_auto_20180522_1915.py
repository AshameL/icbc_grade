# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20180522_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
