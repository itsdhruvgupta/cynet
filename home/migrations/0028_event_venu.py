# Generated by Django 4.0.1 on 2022-05-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_event_contact_number_event_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venu',
            field=models.CharField(default='', max_length=100),
        ),
    ]
