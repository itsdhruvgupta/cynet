# Generated by Django 4.0.1 on 2022-05-01 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_descord_event_name_of_coordinator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='game',
        ),
    ]
