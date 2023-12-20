from django.db import models


class Utente(models.Model):
    username = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Prodotto(models.Model):
    nome_prodotto = models.CharField(max_length=100)
    tipologia = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=75)
    prezzo = models.FloatField(default=0.0)
    quantita = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_prodotto


class Carrello(models.Model):
    utente = models.OneToOneField(Utente, on_delete=models.CASCADE)
    prodotti = models.ManyToManyField(Prodotto, through='CarrelloProdotto')

    def __str__(self):
        return f"Carrello di {self.utente.username}"


class Ordine(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    data_ordine = models.DateTimeField(auto_now_add=True)
    importo_totale = models.FloatField(default=0.0)

    def __str__(self):
        return f"Ordine di {self.utente.username}"


class CarrelloProdotto(models.Model):
    carrello = models.ForeignKey(Carrello, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField(default=1)
    ordine = models.ForeignKey(
        Ordine, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.carrello.utente.username} - {self.prodotto.nome_prodotto} - {self.quantita}"
