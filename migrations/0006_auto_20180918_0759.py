# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0005_auto_20180918_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='condition',
            field=models.CharField(default=b'OR', max_length=3),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dss_pharos.Case', null=True),
        ),
    ]
