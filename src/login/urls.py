from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.login, name="login"),
    #Consertar login
]