# Generated by Django 3.1.5 on 2021-01-25 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("opcalendar", "0019_auto_20210125_1005"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventimport",
            options={
                "verbose_name": "NPSI Event Import",
                "verbose_name_plural": "NPSI Event Imports",
            },
        ),
    ]
