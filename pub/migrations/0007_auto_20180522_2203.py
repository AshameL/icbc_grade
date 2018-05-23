# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0006_auto_20180522_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jud_emp',
            name='papergrade',
        ),
        migrations.RemoveField(
            model_name='jud_emp',
            name='totalgrade',
        ),
        migrations.AddField(
            model_name='employee',
            name='grade',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='papergrade',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='totalgrade',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='jud_emp',
            name='grade',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
