# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0002_engineer_lastname'),
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_o', models.BigIntegerField(max_length=10)),
                ('name', models.CharField(max_length=300)),
                ('housing', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('direction', models.TextField(max_length=999)),
                ('slug', models.SlugField()),
                ('engineer', models.ForeignKey(to='engineer.engineer')),
                ('parish', models.ForeignKey(to='Location.parish')),
            ],
            options={
                'db_table': 'housing',
            },
        ),
    ]
