# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0004_auto_20180522_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='num',
        ),
    ]
