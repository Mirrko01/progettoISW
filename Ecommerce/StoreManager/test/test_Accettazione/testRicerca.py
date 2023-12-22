from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Prodotto
import unittest


class ricercaTest(unittest.TestCase):

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
        username.send_keys("pippo")

        password = self.browser.find_element(
            By.NAME, "password")
        password.send_keys("password123@")

        # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "loginButton")
        submit_button.click()

        self.browser.get("http://localhost:8000/prodotti")
        wait = WebDriverWait(self.browser, 10)

        # Compila il form di ricerca del prodotto
        tipologia = self.browser.find_element(
            By.NAME, "tipologia")
        tipologia.clear()
        tipologia.send_keys("cibo")

        prezzoMinimo = self.browser.find_element(
            By.NAME, "prezzo_minimo")
        prezzoMinimo.send_keys(0.0)

        prezzoMassimo = self.browser.find_element(
            By.NAME, "prezzo_massimo")
        prezzoMassimo.clear()
        prezzoMassimo.send_keys(20.0)

        search_button = self.browser.find_element(
            By.NAME, "cerca")
        search_button.click()


        wait = WebDriverWait(self.browser, 10)
    