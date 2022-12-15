from django.shortcuts import render
from django.db import connection


# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def centros(request):
    return render(request, 'app/centros.html')

def login(request):
    return render(request, 'app/login.html')

def hora(request):
    return render(request, 'app/hora.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def especialistas(request): 
    return render(request, 'app/especialistas.html')

def administracion(request):
    return render(request, 'app/administracion.html')

def pago (request):
    return render(request, 'app/pago.html')

def test(request):
    data = {
        'pacientes': lista_pacientes(),  
    }
    return render(request, 'app/test.html',data)
    
#---------------------------------------------------------------
#PROCEDIMIENTOS ALMACENADOS

def lista_pacientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    out_cur = django_cursor.connection.cursor()  #recibe
    
    cursor.callproc('sp_listar_pacientes', [out_cur]) #llama al procedimiento almacenado
    
    listaPaci = []
    for fila in out_cur:
        listaPaci.append(fila)
        
    return listaPaci
    
    