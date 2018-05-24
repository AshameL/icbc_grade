# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0011_delete_onpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ave_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='papergrade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='totalgrade',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
