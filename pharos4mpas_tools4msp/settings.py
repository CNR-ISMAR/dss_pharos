# -*- coding: utf-8 -*-
import os
import sys
import apps
PROJECT_ROOT = os.path.dirname(__file__)


SITE_NAME = 'DSS Pharos For MPAs'

DEBUG=True

ROOT_URLCONF = 'pharos4mpas_tools4msp.urls'

#TEMPLATES = [
#{
#	'APP_DIRS' : True
#},
#]

SECRET_KEY ='9kdS`tqk0!<vW~YqxS9J]oMZT0gu?*K0^B8`X?E4i:csiJAWG'


INSTALLED_APPS = (

#    'modeltranslation',

    # Boostrap admin theme
    # 'django_admin_bootstrapped.bootstrap3',
    # 'django_admin_bootstrapped',

    # Apps bundled with Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',

    # Utility
    'bootstrap3_datetime',
#    'django_filters',
#    'django_basic_auth',
#    'autocomplete_light',

    # Theme
    'django_forms_bootstrap',


    # login with external providers
#    'allauth',
#    'allauth.account',
#    'allauth.socialaccount',
'apps.dss_pharos', 
'ckeditor',
'ckeditor_uploader', 
'django_bootstrap_breadcrumbs',
)
CKEDITOR_UPLOAD_PATH = 'cked_upload'

STATIC_URL='/static/'
ALLOWED_HOSTS = ['pharos4mpas.tools4msp.eu', 'data.adriplan.eu', 'localhost']
