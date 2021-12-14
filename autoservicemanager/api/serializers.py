from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Car, Transaction, ClientCard
from django.db.models import Sum


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "groups",
        ]


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "model",
            "an_achizitie",
            "nr_km",
            "in_garantie",
            "suma_manopera",
        ]


class ClientCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCard
        fields = [
            "id",
            "nume",
            "prenume",
            "CNP",
            "data_nasterii",
            "data_inregistrarii",
            "reducere_client",
        ]


class TranzactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "id_masina",
            "id_client_card",
            "data_si_ora",
            "suma_piese",
            "suma_manopera",
            "suma_piese_plata",
            "suma_manopera_plata",
            "reducere_manopera",
            "reducere_piese",
            "reducere_totala",
        ]
