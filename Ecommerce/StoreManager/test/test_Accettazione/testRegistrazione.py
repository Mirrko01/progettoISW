from selenium import webdriver
import time
import unittest

class RegistrazioneClienteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_registrazione_cliente(self):
        # Apri la pagina di registrazione
        self.driver.get("http://localhost:8000/registrazione")  # Sostituisci con l'URL effettivo

        # Compila il form di registrazione
        username = self.driver.find_element_by_name("username")
        username.send_keys("nuovo_cliente")

        password = self.driver.find_element_by_name("password")
        password.send_keys("password123")

        email = self.driver.find_element_by_name("email")
        email.send_keys("nuovo_cliente@example.com")

        nome = self.driver.find_element_by_name("nome")
        nome.send_keys("Nuovo")

        cognome = self.driver.find_element_by_name("cognome")
        cognome.send_keys("Cliente")

        telefono = self.driver.find_element_by_name("telefono")
        telefono.send_keys("1234567890")

        # Invia il form
        submit_button = self.driver.find_element_by_name("registrazione_button")
        submit_button.click()

        # Verifica che l'account sia stato creato
        success_message = self.driver.find_element_by_css_selector(".success-message").text
        self.assertIn("Account creato con successo", success_message)

        # Verifica che l'accesso sia avvenuto automaticamente
        logged_in_username = self.driver.find_element_by_css_selector(".logged-in-username").text
        self.assertEqual("nuovo_cliente", logged_in_username)