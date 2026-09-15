from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Comando de prueba para verificar estructura'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('El comando cargar_socios funciona correctamente'))
