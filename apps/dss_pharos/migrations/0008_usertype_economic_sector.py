# Generated by Django 2.2.6 on 2019-10-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0007_remove_impact_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='economic_sector',
            field=models.ManyToManyField(to='dss_pharos.EconomicSector'),
        ),
    ]