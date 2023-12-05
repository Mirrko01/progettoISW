from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.registrazione, name="registrazione"),
    path("registrazione/", views.registrazione, name="registrazione"),
    path("login/", views.login_user, name="login"),
    path("prodotti/", views.prodotti, name="prodotti"),
    path("logout/", views.logout_user, name="logout"),
    path("carrello/", views.visualizza_carrello, name="carrello"),
    path('aggiungi_al_carrello/<int:prodotto_id>/',
         views.aggiungi_al_carrello, name='aggiungi_al_carrello'),
    path('rimuovi_dal_carrello/<int:prodotto_id>/',
         views.rimuovi_dal_carrello, name='rimuovi_dal_carrello'),
    path("checkout/", views.checkout, name="checkout"),
    path("effettua_ordine/", views.effettua_ordine, name="effettua_ordine"),
    path("dashboard/", views.dashboard, name="dashboard"),


]
