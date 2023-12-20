from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Utente
import unittest


class RegistrazioneClienteTest(unittest.TestCase):

    def cancellaUtenti(self):
        Utente.Objects.all().delete()

    def setUp(self):
        # Sostituisci con il tuo percorso per chromebrowser
        self.browser = webdriver.Chrome()

    def test_registrazione_cliente(self):
        # Apri la pagina di registrazione
        self.browser.get("http://localhost:8000/registrazione")

        # Compila il form di registrazione
        username = self.browser.find_element(
            By.NAME, "username")
        username.send_keys("pippo")

        # Assicurati di utilizzare il nome corretto per il campo della password
        password = self.browser.find_element(
            By.NAME, "password1")
        password.send_keys("password123@")

        # Assicurati di utilizzare il nome corretto per il campo di conferma della password
        password_confirm = self.browser.find_element(
            By.NAME, "password2")
        password_confirm.send_keys("password123@")

        email = self.browser.find_element(
            By.NAME, "email")
        email.send_keys("pippo@example.com")

        # Assicurati di utilizzare il nome corretto per il campo del nome
        nome = self.browser.find_element(
            By.NAME, "nome")
        nome.send_keys("Nuovo")

        # Assicurati di utilizzare il nome corretto per il campo del cognome
        cognome = self.browser.find_element(
            By.NAME, "cognome")
        cognome.send_keys("Cliente")

        telefono = self.browser.find_element(
            By.NAME, "telefono")
        telefono.send_keys("1234567890")

        # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "registrazione_button")
        submit_button.click()

        wait = WebDriverWait(self.browser, 10)
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")))

        # Verifica che il testo del messaggio di successo contenga la stringa desiderata
        self.assertIn("Account creato con successo", success_message.text)
