# Generated by Django 3.1.2 on 2021-01-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("opcalendar", "0011_eventimport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventimport",
            name="source",
            field=models.CharField(
                choices=[
                    ("Spectre Fleet", "Spectre Fleet"),
                    ("EVE University", "EVE University"),
                ],
                max_length=32,
            ),
        ),
    ]
