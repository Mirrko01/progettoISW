from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.registrazione, name="registrazione"),
    path("registrazione/", views.registrazione, name="registrazione"),
]
