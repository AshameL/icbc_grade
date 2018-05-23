# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0007_auto_20180522_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='grade',
        ),
    ]
