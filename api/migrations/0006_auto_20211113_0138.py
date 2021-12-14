# Generated by Django 3.2.9 on 2021-11-12 23:38

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_cars_suma_manopera"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="suma_manopera",
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
        migrations.AlterField(
            model_name="transactions",
            name="suma_piese",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[
                    api.validators.stringvalidator,
                    api.validators.validate_positive,
                ],
            ),
        ),
    ]
