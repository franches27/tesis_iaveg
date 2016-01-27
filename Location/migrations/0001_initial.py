# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'municipality',
            },
        ),
        migrations.CreateModel(
            name='parish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('municipality', models.ForeignKey(to='Location.municipality')),
            ],
            options={
                'db_table': 'parish',
            },
        ),
        migrations.CreateModel(
            name='sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('parish', models.ForeignKey(to='Location.parish')),
            ],
            options={
                'db_table': 'sector',
            },
        ),
    ]
