# Generated by Django 3.1.2 on 2021-03-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opcalendar', '0034_auto_20210314_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_visibility',
        ),
        migrations.AddField(
            model_name='event',
            name='event_visibility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='opcalendar.eventvisibility'),
        ),
    ]