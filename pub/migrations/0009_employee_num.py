# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0008_remove_employee_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
