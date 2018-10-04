# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0008_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_description',
            new_name='description',
        ),
    ]
