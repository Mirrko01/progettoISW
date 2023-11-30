from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.registrazione, name="registrazione"),
    path("registrazione/", views.registrazione, name="registrazione"),
    path("login/", views.login_user, name="login"),
    path("prodotti/", views.prodotti, name="prodotti"),
    path("logout/", views.logout_user, name="logout"),


    path("base/", views.base, name="base"),

]
