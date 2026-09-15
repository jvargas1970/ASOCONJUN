import pandas as pd
from django.core.management.base import BaseCommand
from socios.models import Socio

class Command(BaseCommand):
    help = 'Importa socios desde un archivo Excel'

    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str, help='Ruta del archivo Excel')

    def handle(self, *args, **kwargs):
        archivo = kwargs['archivo']
        df = pd.read_excel(archivo)

        for _, row in df.iterrows():
            # Validar que la fila tenga fecha
            if pd.isna(row['fecha_ingreso']):
                self.stdout.write(self.style.WARNING(f"Fila omitida: {row['nombre']} sin fecha de ingreso"))
                continue

            # Convertir fecha a texto ISO (YYYY-MM-DD)
            fecha = str(row['fecha_ingreso']).split(' ')[0]

            Socio.objects.create(
                cedula=row['cedula'],
                nombre=row['nombre'],
                carnet_colegiado=row['carnet_colegiado'],
                telefono=row['telefono'],
                fecha_ingreso=fecha,
                estado=row['estado'],
                observaciones=row.get('observaciones', '')
            )

        self.stdout.write(self.style.SUCCESS('Socios importados correctamente'))
