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
    data={
        'horaspacientes': listarhorapacientes(),
    }
    
    if request.method == 'POST':
        rut= request.POST.get('rut')
        nombre= request.POST.get('nombre')
        apellidoPaterno= request.POST.get('apellidoPaterno')
        apellidoMaterno= request.POST.get('apellidoMaterno')
        correo= request.POST.get('correo')
        direccion= request.POST.get('direccion')
        telefono= request.POST.get('telefono')
        especialidad= request.POST.get('especialidad')
        fecha= request.POST.get('fecha')
        hora= request.POST.get('hora')
        salida=agregarhorapaciente(rut,nombre,apellidoPaterno,apellidoMaterno,correo,direccion,telefono,especialidad,fecha,hora)
        if salida == 1:
            data['mensaje'] = 'Hora agregada correctamente'
            data['horaspacientes'] = listarhorapacientes()
        else:
            data['mensaje'] = 'Error al agregar hora'
        
       
    
    return render(request, 'app/hora.html',data)

def nosotros(request):
    return render(request, 'app/nosotros.html')

def especialistas(request): 
    return render(request, 'app/especialistas.html')

def administracion(request):
    return render(request, 'app/administracion.html')

def horaspacientes(request):
    print(listarhorapacientes())
    data={
        'horaspacientes': listarhorapacientes(),
    }
    return render(request, 'app/horaspacientes.html',data)



def pago (request):
    data = {
        'pago': lista_pago(),
    }
    
    if request.method == 'POST':
        idpago = request.POST.get('pagoid')
        monto = request.POST.get('monto')
        rut= request.POST.get('rut')
        salida=agregar_pago(idpago,monto,rut)
        if salida == 1:
            data['mensaje'] = 'Pago agregado correctamente'
            data['pago'] = lista_pago()
        else:
            data['mensaje'] = 'Error al agregar pago'
    
    return render(request, 'app/pago.html',data)

def informepago(request):
    print(lista_pago())
    data={
        'pago': lista_pago(),
    }
    
    if request.method == 'POST':
        idpago = request.POST.get('pagoid')
        monto = request.POST.get('monto')
        rut= request.POST.get('rut')
        salida=agregar_pago(idpago,monto,rut)
        if salida == 1:
            data['mensaje'] = 'Pago agregado correctamente'
            data['pago'] = lista_pago()
        else:
            data['mensaje'] = 'Error al agregar pago'
    return render(request, 'app/informepago.html',data)


def calendarios(request):
    print(lista_calendarios())
    data={
        'calendarios': lista_calendarios(),
    }
    
    return render(request, 'app/calendarios.html',data)

def GeneradorCalendariosMedicos(request):
    data={
        'calendarios': lista_calendarios(),
    }
    if request.method == 'POST':
        idCalendarioBase = request.POST.get('idcalendariobase')
        rutmedico= request.POST.get('rutmedico')
        nombreMedico= request.POST.get('nombremedico')
        fecha= request.POST.get('fecha')
        salida=agregarCalendarioMedico(idCalendarioBase,rutmedico,nombreMedico,fecha)
        if salida == 1:
            data['mensaje'] = 'Calendario agregado correctamente'
            data['calendarios'] = lista_calendarios()
        else:
            data['mensaje'] = 'Error al agregar calendario'
            
    return render(request, 'app/GeneradorCalendariosMedicos.html',data)

    


def test(request):
    data = {
        'pacientes': lista_pacientes(),  
    }
    print(data)
    
    
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
  

def lista_pago():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    out_cur2 = django_cursor.connection.cursor()  #recibe
    
    cursor.callproc('sp_listar_pago', [out_cur2]) #llama al procedimiento almacenado
    
    listapago = []
    for fila in out_cur2:
        listapago.append(fila)
        
    return listapago

def agregar_pago(idpago,monto,rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    salida2 = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agr_pago', [idpago,monto,rut,salida2])
    return salida2.getvalue()

# HORA PACIENTES

def listarhorapacientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    out_cur3 = django_cursor.connection.cursor()  #recibe
    
    cursor.callproc('sp_listar_horapaciente', [out_cur3]) #llama al procedimiento almacenado
    
    listahorapaciente = []
    for fila in out_cur3:
        listahorapaciente.append(fila)
        
    return listahorapaciente

def agregarhorapaciente(rut,nombre,apellidoPaterno,apellidoMaterno,correo,direccion,telefono,especialidad,fecha,hora):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    salida3 = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agr_horapaciente', [rut,nombre,apellidoPaterno,apellidoMaterno,correo,direccion,telefono,especialidad,fecha,hora,salida3])
    return salida3.getvalue()

#---------------------------------------------------------------
# Calendarios Medicos

def lista_calendarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    out_cur4 = django_cursor.connection.cursor()  #recibe
    
    cursor.callproc('sp_listar_calendarioMedicos', [out_cur4]) #llama al procedimiento almacenado
    
    listacalendarios = []
    for fila in out_cur4:
        listacalendarios.append(fila)
        
    return listacalendarios



def agregarCalendarioMedico(idCalendarioBase,rutmedico,nombreMedico,fecha):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #llama
    salida4 = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_calendarioMedico', [idCalendarioBase,rutmedico,nombreMedico,fecha,salida4])
    return salida4.getvalue()


