from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    path('validar-carnet/', views.validar_carnet_view, name='validar_carnet'),
    path('registro-form/', views.registro_view, name='registro'),
    path('aprobar/<int:user_id>/', views.aprobar_view, name='aprobar'),

    # Crear usuario
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),

    # Registro y aprobación vía API
    path('registro/', views.registro_view, name='registro_socio'),
    path('aprobar/', views.aprobar_view, name='aprobar_socio'),

    # Registro y aprobación vía vistas HTML
    path('registro-form/', views.registro_view, name='registro'),
    path('aprobar/<int:user_id>/', views.aprobar_view, name='aprobar'),

    # Validación inicial de carnet colegiado
    path('validar-carnet/', views.validar_carnet_view, name='validar_carnet'),
]
