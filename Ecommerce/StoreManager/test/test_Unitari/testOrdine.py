import unittest
import datetime


from StoreManager.models import Ordine
from StoreManager.models import Utente


class testOrdine (unittest.TestCase):
    
    def setUp(self):

        self.utente = Utente(username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "giannimunari@test.com", password = "pippo")
        self.utente.save()

        self.ordine = Ordine(utente=self.utente,data_ordine=datetime.datetime(2023, 9, 10, 0, 0, tzinfo=datetime.timezone.utc),importo_totale=10.0)
        self.ordine.save()

    def testOrdine(self):

        data_odierna = datetime.now()
        data_odierna_format = data_odierna.strftime('%Y-%m-%d')

        self.assertEqual(self.ordine.utente.username,"giannimunari123")
        self.assertEqual(self.ordine.data_ordine.strftime('%Y-%m-%d'), data_odierna_format)
        self.assertEqual(self.ordine.importo_totale,10.0)

    def test_str(self):
        nomeDataOrdine = self.ordine.__str__()
        self.assertEqual(nomeDataOrdine , "Ordine di giannimunari123")
