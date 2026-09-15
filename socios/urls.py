from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from .views import crear_usuario

urlpatterns = [
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
]
from django.urls import path
from .views import registro_socio, aprobar_socio

urlpatterns = [
    path('registro/', registro_socio, name='registro_socio'),
    path('aprobar/', aprobar_socio, name='aprobar_socio'),
]
from django.urls import path
from .views import registro_view, aprobar_view

urlpatterns = [
    path('registro/', registro_view, name='registro'),
    path('aprobar/<int:user_id>/', aprobar_view, name='aprobar'),
]
