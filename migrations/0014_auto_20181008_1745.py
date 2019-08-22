# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0013_auto_20181008_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='name',
            new_name='description',
        ),
    ]
