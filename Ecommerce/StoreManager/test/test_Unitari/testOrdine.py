import unittest

from StoreManager.models import Ordine
from StoreManager.models import Utente


class testOrdine (unittest.TestCase):
    
    def setUp(self):

        self.utente = Utente(username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "giannimunari@test.com", password = "pippo")
        self.utente.save()

        self.ordine = Ordine(utente=self.utente,data_ordine="2023-09-10",importo_totale=10.0)
        self.ordine.save()

    def testOrdine(self):
        self.assertEqual(self.ordine.utente.username,"giannimunari123")
        self.assertEqual(self.ordine.data_ordine,"2023-09-10")
        self.assertEqual(self.ordine.importo_totale,10.0)

    def test_str(self):
        nomeDataOrdine = self.ordine.__str__()
        self.assertEqual(nomeDataOrdine , "Ordine di giannimunari123 - 2023-09-10")
