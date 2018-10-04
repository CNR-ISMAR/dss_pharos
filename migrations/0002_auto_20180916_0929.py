# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='Recommendation_text',
            new_name='recommendation_text',
        ),
    ]
