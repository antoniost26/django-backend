# Generated by Django 3.2.9 on 2021-11-13 02:24

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_transactions_manopera"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transactions",
            old_name="manopera",
            new_name="reducere_manopera",
        ),
        migrations.AddField(
            model_name="transactions",
            name="reducere_piese",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                validators=[
                    api.validators.stringvalidator,
                    api.validators.validate_positive,
                ],
            ),
        ),
    ]
