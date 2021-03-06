# Generated by Django 4.0.1 on 2022-05-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_remove_banner_image_name_remove_event_image_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='contact_number',
            new_name='contact_number_of_coordinator_1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='coordinator_profile',
            new_name='coordinator_1_profile',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='email',
            new_name='email_of_coordinator_1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='images',
            new_name='event_images',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name_of_coordinator',
            new_name='name_of_coordinator_1',
        ),
        migrations.AddField(
            model_name='event',
            name='contact_number_of_coordinator_2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='event',
            name='coordinator_2_profile',
            field=models.ImageField(default='', upload_to='static/'),
        ),
        migrations.AddField(
            model_name='event',
            name='email_of_coordinator_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='name_of_coordinator_2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
