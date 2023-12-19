import unittest

from StoreManager.models import Utente


class testUtente (unittest.TestCase):
    
    def setUp(self):
        self.utente = Utente(username = "giannimunari123", nome = "Gianni", cognome = "Munari", telefono = "333123456", email = "giannimunari@test.com", password = "pippo")
        self.utente.save()
    
    def testUtente (self):
        self.assertEqual(self.utente.username ,"giannimunari123")
        self.assertEqual(self.utente.nome ,"Gianni")
        self.assertEqual(self.utente.cognome ,"Munari")
        self.assertEqual(self.utente.telefono ,"333123456")
        self.assertEqual(self.utente.email ,"giannimunari@test.com")
        self.assertEqual(self.utente.password ,"pippo")

    def test_str(self):
        userUtente = self.utente.__str__()
        self.assertEqual(userUtente , "giannimunari123")
    

