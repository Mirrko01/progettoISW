from django.db import models


class Utente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    password=models.CharField(max_length=30)
    
    #


class Prodotto(models.Model):
    nome_prodotto = models.CharField(max_length=100)
    tipologia = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=150)
    prezzo = models.FloatField(default=0.0)
    quantita = models.IntegerField(default=0)

    # aggiungi funzioni


class Acquisto(models.Model):
    # lista_prodotti=?
    data_acquisto = models.models.DateField()
    indirizzo_spedizione = models.CharField(max_length=100)
    metodo_pagamento = models.CharField(max_length=50)

    # aggiungi funzioni
