# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0002_auto_20180522_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username',
            new_name='name',
        ),
    ]
