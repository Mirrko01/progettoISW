import unittest

from StoreManager.models import Carrello
from StoreManager.models import Utente
from StoreManager.models import Prodotto


class testCarrello (unittest.TestCase):

    def setUp(self):

        self.utente = Utente(username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "giannimunari@test.com", password = "pippo")
        self.utente.save()

        self.prodotto = Prodotto(nome_prodotto="pasta",tipologia="cibo", descrizione="pasta barilla",prezzo=2.0,quantita=1)
        self.prodotto.save()

        self.carrello = Carrello(utente=self.utente,prodotto = self.prodotto)
        self.carrello.save()

    def testCarrello(self):
        self.assertEqual(self.carrello.utente.nome,"Gianni")
        self.assertEqual(self.carrello.utente.username, "giannimunari123")
        self.assertEqual(self.carrello.prodotti.nome_prodotto, "pasta")
        self.assertEqual(self.carrello.prodotti.descrizione, "pasta barilla")

    def test_str(self):
        nomeUtenteCarrello = self.carrello.__str__()
        self.assertEqual(nomeUtenteCarrello , "Carrello di giannimunari123")