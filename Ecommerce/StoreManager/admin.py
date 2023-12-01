from django.contrib import admin
from .models import *

admin.site.register(Utente)
admin.site.register(Prodotto)
admin.site.register(Carrello)
admin.site.register(CarrelloProdotto)
# Register your models here.
