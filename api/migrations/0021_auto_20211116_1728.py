# Generated by Django 3.2.9 on 2021-11-16 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_alter_transaction_id_client_card"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="reducere_manopera",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="reducere_piese",
        ),
    ]