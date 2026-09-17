from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            "cedula", "nombre", "fecha_ingreso", "estado", "observaciones",
            "carnet_colegiado", "telefono",
            "nacionalidad", "estado_civil", "fecha_nacimiento",
            "telefono_fijo", "direccion_habitacion", "email_personal",
            "telefono_oficina", "carrera", "fecha_ingreso_tesorero",
            "direccion_regional", "numero_circuitos", "email_trabajo",
            "actividad_economica", "email_factura"
        ]
