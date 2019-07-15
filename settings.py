# -*- coding: utf-8 -*-

DATABASES.update({'dss_pharos_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dss_pharos',
        'USER': 'dss_pharos',
        'PASSWORD': 'pharos',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
})

SITE_NAME = 'DSS Pharos For MPAs'

TEMPLATES = [

{


	'APP_DIRS' : True

},
]

#ALLOWED_HOSTS = ALLOWED_HOSTS + 'pharos4mpas.tools4msp.eu'
