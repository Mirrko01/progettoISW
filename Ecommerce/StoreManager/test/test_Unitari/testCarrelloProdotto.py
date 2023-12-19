import unittest

from StoreManager.models import Carrello
from StoreManager.models import CarrelloProdotto
from StoreManager.models import Prodotto
from StoreManager.models import Utente
from StoreManager.models import Ordine



class testCarrelloProdotto (unittest.TestCase):

    def setUp(self):
        
        self.utente = Utente(username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "giannimunari@test.com", password = "pippo")
        self.utente.save()

        self.prodotto = Prodotto(nome_prodotto="pasta",tipologia="cibo", descrizione="pasta barilla",prezzo=2.0,quantita=1)
        self.prodotto.save()

        self.carrello = Carrello(utente=self.utente)
        self.carrello.save()

        self.ordine = Ordine(utente=self.utente,data_ordine="2023-09-10",importo_totale=10.0)
        self.ordine.save()

        self.carrelloProdotto = CarrelloProdotto(carrello=self.carrello,prodotto=self.prodotto,quantita=15.0,ordine=self.ordine)
        self.carrelloProdotto.save()

    def testCarrelloProdotto(self):

        self.assertEqual(self.carrelloProdotto.carrello.utente.username,"giannimunari123")
        self.assertEqual(self.carrelloProdotto.prodotto.nome_prodotto, "pasta")
        self.assertEqual(self.carrelloProdotto.quantita, 15.0)
        self.assertEqual(self.carrelloProdotto.ordine.utente.username,"giannimunari123")

    def test_str(self):
        strCarrelloProdotto = self.carrelloProdotto.__str__()
        self.assertEqual(strCarrelloProdotto , "giannimunari123 - pasta - 15.0")