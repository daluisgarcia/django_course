# Generated by Django 3.1.1 on 2020-10-15 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='latitud',
            new_name='latitude',
        ),
    ]
