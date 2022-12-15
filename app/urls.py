from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('centros', centros, name="centros"),
    path('horas', hora, name="hora"),
    path('login', login, name="login"),
    path('nosotros', nosotros, name="nosotros"),
    path('especialistas', especialistas, name="especialistas"),
    path('administracion', administracion, name="administracion"),
    path('pago', pago, name="pago"),
    path('test', test, name="test"),
]
