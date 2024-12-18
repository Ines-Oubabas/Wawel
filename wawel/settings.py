"""
Django settings for wawel project.

Generated by 'django-admin startproject' using Django 5.1.4.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Charge le fichier .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u-x_4xq#^jx74nm94kj3#l#8gz@xwmwjj3=xs_n*n@_40pz%*z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'magasin',  # Ajout de votre application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wawel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Chemin vers les templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wawel.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'fr-ca'  # Français (Canada)

TIME_ZONE = 'America/Montreal'  # Fuseau horaire de Montréal

USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "magasin/static"]  # Chemin vers les fichiers statiques
STATIC_ROOT = BASE_DIR / "staticfiles"  # Pour le déploiement

# Configuration des fichiers médias (images téléchargées)
MEDIA_URL = '/media/'  # URL pour accéder aux fichiers médias
MEDIA_ROOT = BASE_DIR / "media"  # Chemin pour stocker les fichiers médias

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration pour l'envoi d'emails via Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Serveur SMTP de Gmail
EMAIL_PORT = 587  # Port pour TLS
EMAIL_USE_TLS = True  # Utilisation de TLS pour sécuriser l'envoi
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # Remplace par l'adresse email WAWEL
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') # Mot de passe spécifique généré
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'WAWEL <no-reply@example.com>')
  # Nom affiché pour l'expéditeur

