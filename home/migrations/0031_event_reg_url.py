# Generated by Django 4.0.1 on 2022-05-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reg_url',
            field=models.CharField(default='', max_length=100),
        ),
    ]