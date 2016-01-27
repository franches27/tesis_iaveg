# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='lastname',
            field=models.CharField(default='hola', max_length=300),
            preserve_default=False,
        ),
    ]
