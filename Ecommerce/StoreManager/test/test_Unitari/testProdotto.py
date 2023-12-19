import unittest

from StoreManager.models import Prodotto


class testProdotto (unittest.TestCase):

    def setUp(self):
        self.prodotto = Prodotto(nome_prodotto="pasta",tipologia="cibo", descrizione="pasta barilla",prezzo=2,quantita=1)
        self.prodotto.save()
    
    def testProdotto (self):
        self.assertEqual(self.prodotto.nome_prodotto, "pasta")
        self.assertEqual(self.prodotto.tipologia, "cibo")
        self.assertEqual(self.prodotto.descrizione, "pasta barilla")
        self.assertEqual(self.prodotto.prezzo, 2)
        self.assertEqual(self.prodotto.quantita, 1)


    def test_str(self):
        nomeProdotto = self.prodotto.__str__()
        self.assertEqual(nomeProdotto , "pasta")