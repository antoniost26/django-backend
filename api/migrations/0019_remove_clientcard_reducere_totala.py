# Generated by Django 3.2.9 on 2021-11-13 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0018_auto_20211113_1904"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clientcard",
            name="reducere_totala",
        ),
    ]