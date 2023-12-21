from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Prodotto
from StoreManager.models import Prodotto
import unittest


class eliminaProdottoTest(unittest.TestCase):

    def cancellaProdotti(self):
        Prodotto.Objects.all().delete()

    def setUp(self):
        # Sostituisci con il tuo percorso per chromebrowser
        self.browser = webdriver.Chrome()

    def test_registrazione_cliente(self):
        # Apri la pagina di login
        self.browser.get("http://localhost:8000/login")

         # Admin effettua login
        username = self.browser.find_element(
            By.NAME, "username")
        username.send_keys("admin1")
 
        password = self.browser.find_element(
            By.NAME, "password")
        password.send_keys("admin1@")

         # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "loginButton")
        submit_button.click()

        self.browser.navigate().to("http://localhost:8000/prodotti")

        #L'admin sceglie il prodotto da modificare
        link_modifica = self.browser.find_element(
            By.NAME, "modifica")
        link_modifica.click()

       #L'admin clicca sul link di eliminazione del prodotto

        wait = WebDriverWait(self.browser, 10)
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")))
    
        self.assertIn("Prodotto eliminato con successo!", success_message.text)