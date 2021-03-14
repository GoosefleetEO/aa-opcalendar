# Generated by Django 3.1.2 on 2021-03-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('opcalendar', '0025_eventvisibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='restricted_to_group',
            field=models.ManyToManyField(blank=True, help_text='Restrict ping rights to the following group(s) ...', related_name='webhook_require_groups', to='auth.Group'),
        ),
    ]