import unittest

from StoreManager.models import Carrello
from StoreManager.models import CarrelloProdotto
from StoreManager.models import Prodotto
from StoreManager.models import Utente
from StoreManager.models import Ordine



class testCarrelloProdotto (unittest.TestCase):

    def setUp(self):
        # Creare un utente di esempio
        self.utente = Utente.objects.create(
            username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "pippo@test.com", password = "pippo")

        # Creare un carrello associato all'utente
        self.carrello = Carrello.objects.create(utente=self.utente)

        # Creare un prodotto di esempio
        self.prodotto = Prodotto.objects.create(
            nome_prodotto='Pasta', tipologia='Cibo', descrizione='Pasta Barilla', prezzo=2.0, quantita=10)

        # Creare un ordine di esempio
        self.ordine = Ordine.objects.create(
            utente=self.utente, data_ordine='2023-01-01')

    def test_str(self):
        # Creare un oggetto CarrelloProdotto di esempio
        carrello_prodotto = CarrelloProdotto.objects.create(
            carrello=self.carrello, prodotto=self.prodotto, quantita=3, ordine=self.ordine)

        # Verificare che il metodo __str__ restituisca la stringa attesa
        expected_str = f"{self.utente.username} - {self.prodotto.nome_prodotto} - 3"
        self.assertEqual(str(carrello_prodotto), expected_str)

    # Aggiungi altri metodi di test secondo necessità
        
    def tearDown(self):
        # Elimina gli oggetti di test
        Utente.objects.all().delete()
        Prodotto.objects.all().delete()
        Carrello.objects.all().delete()