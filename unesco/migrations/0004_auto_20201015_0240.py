# Generated by Django 3.1.1 on 2020-10-15 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_auto_20201015_0228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='areaHectares',
            new_name='area_hectares',
        ),
    ]