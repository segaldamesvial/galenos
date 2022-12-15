from django.shortcuts import render
from django.db import connection
import cx_Oracle


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
    
    
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fechanacimiento = request.POST.get('fecha_nacimiento')
        correo= request.POST.get('correo')
        direccion= request.POST.get('direccion')
        celular= request.POST.get('celular')
        salida=agregarPaciente(rut,nombre,apellido,fechanacimiento,correo,direccion,celular)
        if salida == 1:
            data['mensaje'] = 'Paciente agregado correctamente'
            data['pacientes'] = lista_pacientes()
        else:
            data['mensaje'] = 'Error al agregar paciente'
        
        
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


def agregarPaciente(rut,nombre,apellido,fechanacimiento,correo,direccion,celular):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agr_paciente', [rut,nombre,apellido,fechanacimiento,correo,direccion,celular,salida])
    return salida.getvalue()
  