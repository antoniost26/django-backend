import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Car, ClientCard, Transaction


# Create your tests here.
class CarsViewSetTestCase(APITestCase):

    list_url = reverse("cars-list")

    def setUp(self) -> Car:
        self.car = Car.objects.create(
            model="Skoda", an_achizitie=2000, nr_km=2020
        )

    def test_car_list(self) -> Car:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_detail(self) -> Car:
        response = self.client.get(reverse("cars-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["model"], "Skoda")

    def test_car_update(self) -> Car:
        response = self.client.put(
            reverse("cars-detail", kwargs={"pk": 1}),
            {"model": "Skoda", "an_achizitie": 2001, "nr_km": 2020},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {
                "id": 1,
                "in_garantie": False,
                "model": "Skoda",
                "an_achizitie": 2001,
                "nr_km": 2020,
                "suma_manopera": 0,
            },
        )

    def test_car_delete(self) -> Car:
        response = self.client.delete(reverse("cars-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ClientCardsViewSetTestCase(APITestCase):

    list_url = reverse("cards-list")

    def setUp(self) -> ClientCard:
        self.clientCard = ClientCard.objects.create(
            nume="Stan",
            prenume="Antonio",
            CNP=5020826245085,
            data_nasterii="2002-08-26",
        )

    def test_cards_list(self) -> ClientCard:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cards_detail(self) -> ClientCard:
        response = self.client.get(reverse("cards-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nume"], "Stan")

    def test_cards_update(self) -> ClientCard:
        response = self.client.put(
            reverse("cards-detail", kwargs={"pk": 1}),
            {
                "nume": "Stan",
                "prenume": "Gabriel",
                "CNP": 5020826245085,
                "data_nasterii": "2002-08-26",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {
                "id": 1,
                "nume": "Stan",
                "prenume": "Gabriel",
                "CNP": 5020826245085,
                "data_nasterii": "2002-08-26",
                "data_inregistrarii": "2021-12-08",
                "reducere_client": 0,
            },
        )

    def test_cards_delete(self) -> ClientCard:
        response = self.client.delete(
            reverse("cards-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TransactionsViewSetTestCase(APITestCase):

    list_url = reverse("transactions-list")

    def setUp(self) -> Transaction:
        CarsViewSetTestCase.setUp
        self.transaction = Transaction.objects.create(
            id_masina=Car.objects.create(
                model="Skoda", an_achizitie=2000, nr_km=2020
            ),
            suma_piese=200,
            suma_manopera=300,
        )

    def test_transaction_list(self) -> Transaction:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transaction_detail(self) -> Transaction:
        response = self.client.get(
            reverse("transactions-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id_masina"], 1)

    def test_transaction_update(self) -> Transaction:
        response = self.client.put(
            reverse("transactions-detail", kwargs={"pk": 1}),
            {"id_masina": 1, "suma_piese": 200, "suma_manopera": 300},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            {
                "id": 1,
                "id_masina": 1,
                "id_client_card": None,
                "reducere_manopera": 0,
                "reducere_piese": 0,
                "reducere_totala": 0,
                "suma_manopera": "300.00",
                "suma_manopera_plata": 300.0,
                "suma_piese": "200.00",
                "suma_piese_plata": 200.0,
                "data_si_ora": json.loads(response.content)["data_si_ora"],
            },
        )

    def test_transaction_delete(self) -> Transaction:
        response = self.client.delete(
            reverse("transactions-detail", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
