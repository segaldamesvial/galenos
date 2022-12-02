from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('centros', centros, name="centros"),
    path('horas', hora, name="hora"),
    path('login', login, name="login"),
]
