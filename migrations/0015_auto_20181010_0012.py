# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0014_auto_20181008_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
