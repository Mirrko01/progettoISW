import unittest

from StoreManager.models import Carrello
from StoreManager.models import CarrelloProdotto
from StoreManager.models import Prodotto
from StoreManager.models import Utente
from StoreManager.models import Ordine


class testCarrelloProdotto (unittest.TestCase):

    def setUp(self):
        # Creare un utente di esempio
        self.utente = Utente(username="giannimunari123", nome="Gianni", cognome="Munari",
                             telefono="33123456", email="pippo@test.com", password="pippo")
        self.utente.save()

        # Creare un carrello associato all'utente
        self.carrello = Carrello(utente=self.utente)
        self.carrello.save()

        # Creare un prodotto di test
        self.prodotto = Prodotto(nome_prodotto="Pasta", tipologia="Cibo",
                                 descrizione="Pasta Barilla", prezzo=2.0, quantita=10)
        self.prodotto.save()

        # Creare un ordine di test
        self.ordine = Ordine(utente=self.utente, data_ordine="2023-01-01")
        self.ordine.save()

    def test_str(self):
        self.carrello_prodotto = CarrelloProdotto(
            carrello=self.carrello, prodotto=self.prodotto, quantita=3, ordine=self.ordine)
        self.carrello_prodotto.save()

        # Verificare che il metodo __str__ restituisca la stringa attesa
        expected_str = f"{
            self.utente.username} - {self.prodotto.nome_prodotto} - 3"
        self.assertEqual(str(self.carrello_prodotto), expected_str)

    # Aggiungi altri metodi di test secondo necessità

    def tearDown(self):
        # Elimina gli oggetti di test
        Utente.objects.all().delete()
        Prodotto.objects.all().delete()
        Carrello.objects.all().delete()
