from django.contrib import admin
from django.urls import path
from Ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstView/', views.firstView),
]
