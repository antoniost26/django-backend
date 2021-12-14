from random import randrange
from django.db.models import Sum, QuerySet
from django_filters.filters import RangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from model_bakery import baker

from .models import Car, ClientCard, Transaction, TransactionDateRangeFilter
from .serializers import (
    ClientCardSerializer,
    UserSerializer,
    CarsSerializer,
    TranzactionSerializer,
)
from django.contrib.auth.models import User
from rest_framework import filters

# Project views


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


#    permission_classes = [permissions.IsAuthenticated]


class CarsViewSet(viewsets.ModelViewSet):
    """
    Modal viewset used for Cars API Endpoint, which allows usage of CRUD
    """

    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "id",
        "model",
        "an_achizitie",
        "nr_km",
    ]

    def create(self, request, *args, **kwargs):
        """
        Edited create/post method to allow
        bulk creation
        """

        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=False, methods=["post"])
    def generate(self, request):
        """
        Custom API Endpoint used for generating
        entities with the help of Baker Model
        *** Not accesible via ViewSet ***
        """

        Cars = baker.make_recipe(
            "api.model_factory.car_recipe",
            _quantity=request.data["numberOfGenerations"],
        )
        serializer = self.get_serializer(
            data=Cars, many=isinstance(Cars, list)
        )
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def customSort(self, request):
        """
        Custom sort method applied to property
        """

        queryset = list(map(lambda x: x,sorted(
            Car.objects.all(), key=lambda sum: sum.suma_manopera, reverse=True
        )))
        serializer = self.get_serializer(
            queryset, many=isinstance(queryset, list)
        )
        return Response(serializer.data)


#    permission_classes = [permissions.IsAuthenticated]


class CardsViewSet(viewsets.ModelViewSet):
    """
    Modal viewset used for Cards API Endpoint, which allows usage of CRUD
    """

    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "id",
        "nume",
        "prenume",
        "CNP",
        "data_nasterii",
    ]

    @action(detail=False, methods=["get"])
    def customSort(self, request):
        """
        Custom sort method applied to property
        """
        queryset = list(map(lambda x: x, sorted(
            ClientCard.objects.all(),
            key=lambda sum: sum.reducere_client,
            reverse=True,
        )))
        serializer = self.get_serializer(
            queryset, many=isinstance(queryset, list)
        )
        return Response(serializer.data)


class TransactionsViewSet(viewsets.ModelViewSet):
    """
    Modal viewset used for Transactions API Endpoint,
    which allows usage of CRUD
    """

    queryset = Transaction.objects.all()
    serializer_class = TranzactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["data_si_ora"]

    @action(detail=False, methods=["delete"])
    def deleteRange(self, request):
        """
        Custom delete method for a given date range
        """
        queryset = TransactionDateRangeFilter(
            {
                "data_si_ora_after": request.data["after"],
                "data_si_ora_before": request.data["before"],
            }
        )
        queryset.qs.delete()
        return Response("Transactions were deleted")

    @action(detail=False, methods=["post", "get"])
    def viewSumRange(self, request):
        """
        Custom get method for a given sum range
        """
        if request.data:
            queryset = [
                transaction
                for transaction in Transaction.objects.all()
                if int(transaction.suma_manopera_plata)
                + int(transaction.suma_piese_plata)
                in range(int(request.data["start"]), int(request.data["end"]))
            ]
            serializer = TranzactionSerializer(queryset, many=True)
            return Response(serializer.data)
        queryset = Transaction.objects.all()
        serializer = TranzactionSerializer(queryset, many=True)
        return Response(serializer.data)
