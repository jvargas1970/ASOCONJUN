"""
Django settings for asoconjun project.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'django-insecure-7+nc_&c134m!q#d4@wuyxr7$t^6c353j$(osq8=6b6uy+up5zs'
DEBUG = False
ALLOWED_HOSTS = ['asoconjun.onrender.com', '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://asoconjun.onrender.com']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'socios',
    'rest_framework',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'asoconjun.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'asoconjun.wsgi.application'

# Base de datos (Render usa DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "asoconjun" / "static"]   # Carpeta donde guardas tus imágenes
STATIC_ROOT = BASE_DIR / "staticfiles"     # Carpeta que Render usa para servir estáticos

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
