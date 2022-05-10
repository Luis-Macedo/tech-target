from django.urls import path
from . import views

urlpatterns = [
    path('cpf/', views.loginCpf, name="loginCpf"),
    path('cnpj/', views.loginCnpj, name="loginCnpj"),
    #Consertar login
]