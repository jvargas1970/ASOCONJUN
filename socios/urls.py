from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Crear usuario
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),

    # Registro y aprobación vía API
    path('registro/', views.registro_socio, name='registro_socio'),
    path('aprobar/', views.aprobar_socio, name='aprobar_socio'),

    # Registro y aprobación vía vistas HTML
    path('registro-form/', views.registro_view, name='registro'),
    path('aprobar/<int:user_id>/', views.aprobar_view, name='aprobar'),
]
