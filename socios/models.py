from django.db import models

class Socio(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    carnet_colegiado = models.CharField(max_length=50, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('baja', 'Baja')])
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
