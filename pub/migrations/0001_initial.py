# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('num', models.IntegerField()),
                ('ave_grade', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='jud_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('grade', models.FloatField()),
                ('jud_emp', models.ForeignKey(to='pub.employee')),
                ('jud_id', models.ForeignKey(to='judge.user')),
            ],
        ),
    ]
