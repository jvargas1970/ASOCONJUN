from django.core.management.base import BaseCommand
from socios.models import Socio

class Command(BaseCommand):
    help = 'Lista todos los socios cargados'

    def handle(self, *args, **kwargs):
        for s in Socio.objects.all():
            self.stdout.write(f"{s.cedula} | {s.nombre} | {s.carnet_colegiado} | {s.telefono} | {s.fecha_ingreso} | {s.estado} | {s.observaciones}")
