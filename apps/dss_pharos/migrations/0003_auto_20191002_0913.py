# Generated by Django 2.0.13 on 2019-10-02 09:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0002_auto_20191002_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='economicsector',
            name='interactions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='economicsector',
            name='interactions_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='economicsector',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='economicsector',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
