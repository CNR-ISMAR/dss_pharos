# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0012_auto_20181006_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='description',
            new_name='name',
        ),
        migrations.AddField(
            model_name='activity',
            name='bg_image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='bg_information',
            field=ckeditor.fields.RichTextField(default='Write here the backgrund informations related to the activity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
