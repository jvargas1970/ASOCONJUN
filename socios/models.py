from django.db import models
import datetime

class Socio(models.Model):
    # Campos principales
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(default=datetime.date.today)
    estado = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True, null=True)
    carnet_colegiado = models.CharField(max_length=50, unique=True, default="SIN-CARNET")
    telefono = models.CharField(max_length=20, blank=True, null=True)

    # Campos adicionales
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True)
    direccion_habitacion = models.CharField(max_length=200, blank=True, null=True)
    email_personal = models.EmailField(unique=True, blank=True, null=True)
    telefono_oficina = models.CharField(max_length=20, blank=True, null=True)
    carrera = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso_tesorero = models.DateField(blank=True, null=True)
    direccion_regional = models.CharField(max_length=100, blank=True, null=True)
    numero_circuitos = models.IntegerField(blank=True, null=True)
    email_trabajo = models.EmailField(blank=True, null=True)
    actividad_economica = models.CharField(max_length=100, blank=True, null=True)
    email_factura = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.carnet_colegiado})"
