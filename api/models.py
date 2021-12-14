from datetime import date
from django.db import models
from django.db.models import fields
from django.db.models.fields import BooleanField, DecimalField
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet
from django.db.models import Sum

from .validators import (
    validate_date,
    validate_string,
    validate_positive,
    validate_year,
    stringvalidator,
    validate_cnp,
)


# Project models


class Car(models.Model):
    """
    Set model for cars
    """

    model = models.CharField(max_length=32, validators=[validate_string])
    an_achizitie = models.PositiveIntegerField(validators=[validate_year])
    nr_km = models.PositiveIntegerField()

    @property
    def in_garantie(self) -> BooleanField:
        """
        Checks automatically to see if the car has warranty
        """
        if date.today().year - self.an_achizitie < 3:
            if self.nr_km < 60000:
                return True
        return False

    @property
    def suma_manopera(self) -> DecimalField:
        transaction_list = Transaction.objects.all()
        total = 0
        for transaction in transaction_list:
            if transaction.id_masina == self:
                total += transaction.suma_manopera_plata

        return total

    def __str__(self) -> str:
        """
        Returns id for the ForeignKey used in Transactions
        """
        return str(self.id) + ": " + str(self.model)


class ClientCard(models.Model):
    """
    Set model for client cards
    """

    nume = models.CharField(max_length=32, validators=[validate_string])
    prenume = models.CharField(max_length=32, validators=[validate_string])
    CNP = models.PositiveIntegerField(
        validators=[validate_cnp],
        unique=True,
    )
    data_nasterii = models.DateField(validators=[validate_date])
    data_inregistrarii = models.DateField(auto_now_add=True)

    @property
    def reducere_client(self) -> DecimalField:
        transaction_list = Transaction.objects.all()
        total = 0
        for transaction in transaction_list:
            if transaction.id_client_card == self:
                total += transaction.reducere_totala

        return total

    def __str__(self) -> str:
        return str(self.id) + ": " + self.nume + " " + self.prenume


class Transaction(models.Model):
    """
    Set model for transactions
    """

    id_masina = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name="transactions"
    )
    id_client_card = models.ForeignKey(
        ClientCard,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="transactions",
    )
    suma_piese = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[stringvalidator, validate_positive],
    )
    suma_manopera = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[stringvalidator, validate_positive],
    )
    data_si_ora = models.DateTimeField(auto_now_add=True)

    @property
    def reducere_manopera(self) -> DecimalField:
        """
        Automatically calculates the price reduction
        for workmanship
        """
        if self.id_client_card:
            return float("{:.2f}".format(float(self.suma_manopera) * 0.1))
        return 0

    @property
    def reducere_piese(self) -> DecimalField:
        """
        Automatically calculates the price reduction
        for parts
        """
        if self.id_masina.in_garantie:
            return float("{:.2f}".format(self.suma_piese))

        return 0

    @property
    def reducere_totala(self) -> DecimalField:
        """
        Automatically calculates the sum of price reductions
        """
        return self.reducere_manopera + self.reducere_piese

    @property
    def suma_piese_plata(self) -> DecimalField:
        return float(self.suma_piese) - self.reducere_piese

    @property
    def suma_manopera_plata(self) -> DecimalField:
        return float(self.suma_manopera) - self.reducere_manopera


class TransactionDateRangeFilter(FilterSet):
    """
    Custom filter class for Transaction which
    filters them by a given date range
    """

    data_si_ora = DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = ["data_si_ora"]
