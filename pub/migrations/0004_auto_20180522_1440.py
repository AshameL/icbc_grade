# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0003_auto_20180522_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jud_emp',
            old_name='jud_emp',
            new_name='emp_id',
        ),
        migrations.AlterUniqueTogether(
            name='jud_emp',
            unique_together=set([('jud_id', 'emp_id')]),
        ),
    ]
