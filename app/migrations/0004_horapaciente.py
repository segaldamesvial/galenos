# Generated by Django 4.0.5 on 2022-12-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pago_idpago'),
    ]

    operations = [
        migrations.CreateModel(
            name='horaPaciente',
            fields=[
                ('rut', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('especialidad', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=6)),
            ],
        ),
    ]
