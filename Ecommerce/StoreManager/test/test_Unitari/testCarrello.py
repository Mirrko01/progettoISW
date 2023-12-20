import unittest

from StoreManager.models import Carrello
from StoreManager.models import Utente
from StoreManager.models import Prodotto
from StoreManager.models import CarrelloProdotto


class testCarrello (unittest.TestCase):

    def setUp(self):
        # Crea un utente di test
        self.utente = Utente.objects.create(
            username="testuser",
            nome="Test",
            cognome="User",
            telefono="123456789",
            email="testuser@example.com",
            password="testpassword"
        )

        # Crea un prodotto di test
        self.prodotto = Prodotto.objects.create(
            nome_prodotto="Prodotto di Test",
            tipologia="Test",
            descrizione="Descrizione di test",
            prezzo=10.00,
            quantita=1
        )

    def test_carrello_str(self):
        # Crea un carrello di test associato all'utente
        carrello = Carrello.objects.create(utente=self.utente)

        # Verifica che il metodo __str__ restituisca una stringa appropriata
        self.assertEqual(str(carrello), f"Carrello di {self.utente.username}")

    def test_aggiungi_prodotto_al_carrello(self):
        # Crea un carrello di test associato all'utente
        carrello = Carrello.objects.create(utente=self.utente)

        # Aggiungi il prodotto al carrello
        carrello.prodotti.add(self.prodotto)

        # Verifica che il prodotto sia presente nel carrello
        self.assertTrue(carrello.prodotti.filter(pk=self.prodotto.pk).exists())

        # Verifica la quantità del prodotto nel carrello
        carrello_prodotto = CarrelloProdotto.objects.get(carrello=carrello, prodotto=self.prodotto)
        self.assertEqual(carrello_prodotto.quantita, 1)

    def tearDown(self):
        # Elimina gli oggetti di test
        Utente.objects.all().delete()
        Prodotto.objects.all().delete()
        Carrello.objects.all().delete()