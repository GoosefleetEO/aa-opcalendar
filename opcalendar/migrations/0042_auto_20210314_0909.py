# Generated by Django 3.1.2 on 2021-03-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcalendar', '0041_auto_20210314_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
    ]