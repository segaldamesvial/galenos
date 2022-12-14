from django.db import models

# Create your models here.


class Agenda (models.Model):
    idAgenda = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.CharField(max_length=6)
    rutmedico = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nome