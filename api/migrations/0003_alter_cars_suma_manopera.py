# Generated by Django 3.2.9 on 2021-11-12 13:33

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_transactions_id_client_card"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars",
            name="suma_manopera",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                validators=[api.validators.validate_positive],
            ),
        ),
    ]