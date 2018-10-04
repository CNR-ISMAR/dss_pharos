# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0004_recommendation_case'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='case',
        ),
        migrations.AddField(
            model_name='question',
            name='case',
            field=models.ManyToManyField(to='dss_pharos.Case'),
        ),
    ]
