from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Utente
import unittest


class LoginClienteTest(unittest.TestCase):

    def cancellaUtenti(self):
        Utente.Objects.all().delete()

    def setUp(self):
        # Sostituisci con il tuo percorso per chromebrowser
        self.browser = webdriver.Chrome()

    def test_registrazione_cliente(self):
        # Apri la pagina di login
        self.browser.get("http://localhost:8000/login")

        # Compila il form di login
        username = self.browser.find_element(
            By.NAME, "username")
        username.send_keys("pippo")

        # Assicurati di utilizzare il nome corretto per il campo della password
        password = self.browser.find_element(
            By.NAME, "password")
        password.send_keys("password123@")

        # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "loginButton")
        submit_button.click()
