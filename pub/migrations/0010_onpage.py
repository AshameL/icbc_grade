# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0009_employee_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='onpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('thispage', models.CharField(max_length='6')),
            ],
        ),
    ]
