# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ave_grade',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
