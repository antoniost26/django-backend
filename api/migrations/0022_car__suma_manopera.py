# Generated by Django 3.2.9 on 2021-11-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_auto_20211116_1728"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="_suma_manopera",
            field=models.DecimalField(
                db_column="suma_manopera",
                decimal_places=2,
                default=0,
                max_digits=9,
            ),
            preserve_default=False,
        ),
    ]