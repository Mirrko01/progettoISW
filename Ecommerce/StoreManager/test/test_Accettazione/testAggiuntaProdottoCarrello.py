from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Carrello
from StoreManager.models import Utente
from StoreManager.models import CarrelloProdotto
import unittest


class aggiuntaProdottoCarrelloTest(unittest.TestCase):

    def cancellaCarrello(self):
        Carrello.Objects.all().delete()
        CarrelloProdotto.Objects.all().delete()

    def setUp(self):
        # Sostituisci con il tuo percorso per chromebrowser
        self.browser = webdriver.Chrome()

    def test_registrazione_cliente(self):
        # Apri la pagina di login
        self.browser.get("http://localhost:8000/login")

         # Utente effettua login
        username = self.browser.find_element(
            By.NAME, "username")
        username.send_keys("pippo")
 
        password = self.browser.find_element(
            By.NAME, "password")
        password.send_keys("password123@")

         # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "loginButton")
        submit_button.click()

        self.browser.navigate().to("http://localhost:8000/prodotti")

        # Compila il form di aggiunta prodotto
        aggiungi_prodotto = self.browser.find_element(
            By.NAME, "aggiungi")
        aggiungi_prodotto.click()

        wait = WebDriverWait(self.browser, 10)
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")))
        
        utente_pippo = Utente.objects.get(username="pippo")
        
        carrello = Carrello.get(utente = utente_pippo)
        
        carrello_prodotto = CarrelloProdotto.objects.get(carrello = carrello)
        self.assertEqual(carrello_prodotto.quantita, 1)
