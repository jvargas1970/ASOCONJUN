from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # Rutas de la app socios
    path('', include('socios.urls')),
]
