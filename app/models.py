from django.db import models

# Create your models here.


class Agenda (models.Model):
    idAgenda = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.CharField(max_length=6)
    rutmedico = models.CharField(max_length=20)
    
class Cajero (models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    rol = models.CharField(max_length=20)
    
class CalendarioBase (models.Model):
    idCalendarioBase = models.AutoField(primary_key=True)
    fecha = models.DateField()

class HoraMedica (models.Model):
    idhoraMedica = models.AutoField(primary_key=True)
    Hora = models.CharField(max_length=6)
    dia= models.DateField()
    rut= models.CharField(max_length=20)
    
    
class Informe (models.Model):
    idInforme = models.AutoField(primary_key=True)
    fecha = models.DateField()
    contenido = models.CharField(max_length=900)

class Medico (models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    rol = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)

class Paciente (models.Model):
    rut= models.CharField(primary_key=True, max_length=20)
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    fechaNacimiento= models.DateField()
    correo= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    celular= models.IntegerField()
    
class Pago (models.Model):
    idPago= models.IntegerField(primary_key=True)
    monto= models.IntegerField()
    rut= models.CharField(max_length=20)

class Secretaria (models.Model):
    rol= models.CharField(max_length=20)
    rut= models.CharField(primary_key=True, max_length=20)

class Trabajador (models.Model):
    rut= models.CharField(primary_key=True, max_length=20)
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    fechaNacimiento= models.DateField()
    correo= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    telefono= models.IntegerField()
    rol= models.CharField(max_length=20)


class horaPaciente (models.Model):
    rut= models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    correo= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    telefono= models.IntegerField()
    especialidad= models.CharField(max_length=50)
    fecha= models.DateField()
    hora= models.CharField(max_length=6)
    


    
    
# relaciones entre clases 

# trabajador - secretaria
# trabajador = models.ForeignKey(Trabajador, on_delete=models.PROTECT)