# Generated by Django 3.2.9 on 2021-11-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_remove_clientcard_reducere_totala"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="id_client_card",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET(""),
                related_name="transactions",
                to="api.clientcard",
            ),
        ),
    ]
