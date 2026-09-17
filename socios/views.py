from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Socio
from .forms import SocioForm

# Página principal
def index(request):
    socios = Socio.objects.all()
    return render(request, 'socios/index.html', {'socios': socios})

# Validación inicial de carnet colegiado
def validar_carnet_view(request):
    if request.method == 'POST':
        carnet = request.POST.get('carnet_colegiado')
        if not carnet:
            messages.error(request, "Debe ingresar un carnet válido.")
            return render(request, 'socios/validar_carnet.html')

        carnet = carnet.strip()  # elimina espacios

        try:
            socio_existe = Socio.objects.filter(carnet_colegiado=carnet).exists()
            usuario_existe = User.objects.filter(username=carnet).exists()

            if socio_existe and not usuario_existe:
                return render(request, 'socios/registro_usuario.html', {'carnet': carnet})
            elif usuario_existe:
                return render(request, 'socios/login_existente.html', {'carnet': carnet})
            else:
                return render(request, 'socios/no_afiliado.html', {'carnet': carnet})

        except Exception as e:
            messages.error(request, f"Error al validar el carnet: {e}")
            return render(request, 'socios/validar_carnet.html')

    return render(request, 'socios/validar_carnet.html')

# Registro vía formulario web
def registro_view(request):
    if request.method == 'POST':
        carnet = request.POST.get('carnet_colegiado')
        try:
            socio = Socio.objects.get(carnet_colegiado=carnet)
            return render(request, 'socios/registro_existente.html', {"socio": socio})
        except Socio.DoesNotExist:
            form = SocioForm(request.POST or None, initial={
                "carnet_colegiado": carnet,
                "fecha_ingreso": timezone.now().date()
            })
            if form.is_valid():
                form.save()
                messages.success(request, "Socio registrado exitosamente. Pendiente de aprobación.")
                return redirect('registro')
            return render(request, 'socios/registro_nuevo.html', {"form": form})

    return render(request, 'socios/registro_buscar.html')

# Aprobar socio (solo administradores)
def aprobar_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, f"Usuario {user.username} aprobado correctamente.")
    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado.")
    return redirect('/admin/auth/user/')

# Crear usuario (solo administradores, vía API)
@api_view(['POST'])
@permission_classes([IsAdminUser])
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

    user = User.objects.create_user(username=username, password=password, email=email)

    if rol == "admin":
        user.is_staff = True
    else:
        user.is_staff = False

    user.save()
    return Response({"success": f"Usuario {username} creado con rol {rol}"})
