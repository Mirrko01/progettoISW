from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from StoreManager.models import Prodotto
import unittest


class modificaProdottoTest(unittest.TestCase):

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

        # Compila il form di modifica del prodotto
        nome_prodotto = self.browser.find_element(
            By.NAME, "nomeProdotto")
        nome_prodotto.send_keys("carne")

        tipologia = self.browser.find_element(
            By.NAME, "tipologia")
        tipologia.send_keys("cibo")

        descrizione = self.browser.find_element(
            By.NAME, "descrizione")
        descrizione.send_keys("Carne di manzo")

        quantita = self.browser.find_element(
            By.NAME, "quantita")
        quantita.send_keys(1)

        prezzo = self.browser.find_element(
            By.NAME, "prezzo")
        prezzo.send_keys(5)


        # Invia il form
        submit_button = self.browser.find_element(
            By.NAME, "modificaProdotto")
        submit_button.click()

        wait = WebDriverWait(self.browser, 10)
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")))
    
        prodotto_aggiunto = Prodotto.objects.get(nome_prodotto="carne")

        self.assertEqual(prodotto_aggiunto.descrizione,"Carne di manzo")