# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_remove_housing_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='id_o',
            field=models.BigIntegerField(),
        ),
    ]
