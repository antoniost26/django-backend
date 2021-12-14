# Generated by Django 3.2.9 on 2021-11-13 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_clientcard_reducere_totala"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="id_masina",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transactions",
                to="api.cars",
            ),
        ),
    ]
