# Generated by Django 4.0.1 on 2022-05-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_event_coordinator_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winners',
            old_name='game',
            new_name='event_name',
        ),
    ]