# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0005_remove_employee_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='jud_emp',
            name='papergrade',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='jud_emp',
            name='totalgrade',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='jud_emp',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]
