from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Ordine
import unittest


class checkoutTest(unittest.TestCase):

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

        self.browser.get("http://localhost:8000/checkout")
        wait = WebDriverWait(self.browser, 10)

        # Compila il form per il checkout
        metodo_pagamento = self.browser.find_element(
            By.NAME, "metodoPagamento")
        metodo_pagamento.clear()
        metodo_pagamento.send_keys("Carta di credito")

        indirizzo = self.browser.find_element(
            By.NAME, "indirizzo")
        indirizzo.clear()
        indirizzo.send_keys("Via Roma 22")

        # Invia il form
        submit = self.browser.find_element(
            By.NAME, "effettuaOrdine")
        submit.click()

        wait = WebDriverWait(self.browser, 10)
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")))

        # Verifica che il testo del messaggio di successo contenga la stringa desiderata
        self.assertIn('Ordine effettuato con successo!', success_message.text)
