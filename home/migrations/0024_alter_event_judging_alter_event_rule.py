# Generated by Django 4.0.1 on 2022-05-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_event_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='judging',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='event',
            name='rule',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
