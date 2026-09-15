from django.shortcuts import render
from .models import Socio

def index(request):
    socios = Socio.objects.all()
    return render(request, 'socios/index.html', {'socios': socios})
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAdminUser])  # Solo administradores pueden crear usuarios
def crear_usuario(request):
    """
    Crear un nuevo usuario y asignar rol.
    Datos esperados en el body JSON:
    {
        "username": "juan",
        "password": "123456",
        "email": "juan@example.com",
        "rol": "admin"  # o "socio"
    }
    """
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    rol = data.get('rol')

    if not username or not password:
        return Response({"error": "Username y password son obligatorios"}, status=400)

    # Crear usuario
    user = User.objects.create_user(username=username, password=password, email=email)

    # Asignar rol
    if rol == "admin":
        user.is_staff = True   # administrador
    else:
        user.is_staff = False  # socio normal

    user.save()

    return Response({"success": f"Usuario {username} creado con rol {rol}"})
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

# Registro de socios (pendientes de aprobación)
@api_view(['POST'])
@permission_classes([AllowAny])  # cualquier persona puede registrarse
def registro_socio(request):
    """
    Registro de un socio pendiente de aprobación.
    Datos esperados:
    {
        "username": "juan",
        "password": "123456",
        "email": "juan@example.com"
    }
    """
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password:
        return Response({"error": "Username y password son obligatorios"}, status=400)

    # Crear usuario desactivado
    user = User.objects.create_user(username=username, password=password, email=email)
    user.is_active = False   # queda pendiente de aprobación
    user.is_staff = False    # rol socio normal
    user.save()

    return Response({"success": f"Usuario {username} registrado. Pendiente de aprobación por un administrador."})


# Aprobación de socios (solo administradores)
@api_view(['POST'])
@permission_classes([IsAdminUser])  # solo administradores pueden aprobar
def aprobar_socio(request):
    """
    Aprobar un socio registrado.
    Datos esperados:
    {
        "username": "juan"
    }
    """
    data = request.data
    username = data.get('username')

    try:
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        return Response({"success": f"Usuario {username} aprobado y activado"})
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=404)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rol = request.POST.get('rol', 'socio')  # por defecto socio

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)

            if rol == 'admin':
                user.is_staff = True   # administrador
                user.is_active = True  # activo inmediatamente
            else:
                user.is_staff = False  # socio normal
                user.is_active = False # pendiente de aprobación

            user.save()
            messages.success(request, f"Registro exitoso como {rol}. Pendiente de aprobación si es socio.")
            return redirect('registro')

    return render(request, 'registro.html')
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)  # solo administradores
def aprobar_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, f"Usuario {user.username} aprobado")
    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado")
    return redirect('/admin/auth/user/')

from django.http import HttpResponse

