# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='engineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('ci', models.IntegerField(max_length=10)),
                ('civ', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.IntegerField(max_length=12)),
                ('direction', models.TextField(max_length=500)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'engineer',
            },
        ),
    ]
