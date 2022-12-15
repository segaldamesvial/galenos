# Generated by Django 4.0.5 on 2022-12-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_horapaciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarioMedico',
            fields=[
                ('idCalendarioBase', models.IntegerField(primary_key=True, serialize=False)),
                ('rutmedico', models.CharField(max_length=20)),
                ('nombreMedico', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
    ]