# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0010_onpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='onpage',
        ),
    ]
