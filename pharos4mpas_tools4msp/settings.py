"""
Django settings for pharos4mpas_tools4msp project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# -*- coding: utf-8 -*-
import os
import sys
import apps
PROJECT_ROOT = os.path.dirname(__file__)


SITE_NAME = 'DSS Pharos For MPAs'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ixy+byt$7z%mufc-5^r^k179osu!lgi!8p5(&u+b9o4-x1rq@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'pharos4mpas.tools4msp.eu/', 'data.adriplan.eu', '192.168.1.73', '150.178.42.73',]

ROOT_URLCONF = 'pharos4mpas_tools4msp.urls'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'autocomplete-light',
    'dal',
    'dal_select2',

    # dss pharos
    'django_extensions',
    'django.contrib.sites',
    #'account',
    'ckeditor',
    'ckeditor_uploader',
    'django_bootstrap_breadcrumbs',
    'apps.dss_pharos',
    
    
    # Social
    'avatar',
    
    # login with external providers
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

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

ROOT_URLCONF = 'pharos4mpas_tools4msp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'pharos4mpas_tools4msp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
#MEDIA_URL = STATIC_URL + 'uploads/'
MEDIA_ROOT = STATIC_ROOT + 'uploads/'
CKEDITOR_UPLOAD_PATH = 'cked_uploads/'

#DATABASE_ENGINE = 'postgresql_psycopg2'
# DATABASE_NAME = 'pharos4mpas_tools4msp'
# DATABASE_USER = 'geonode'
# DATABASE_PASSWORD = 'TQRULQkX'
# DATABASE_HOST = 'localhost'
# DATABASE_PORT = '5432'

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': DATABASE_NAME,
        # 'USER': DATABASE_USER,
        # 'PASSWORD': DATABASE_PASSWORD,
        # 'HOST': DATABASE_HOST,
        # 'PORT': DATABASE_PORT,
    # },
# }
try:
    from local_settings import *
except ImportError:
    pass
