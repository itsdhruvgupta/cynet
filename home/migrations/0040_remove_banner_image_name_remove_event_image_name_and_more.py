# Generated by Django 4.0.1 on 2022-05-01 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_rename_game_winners_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='winners',
            name='profile_name',
        ),
    ]