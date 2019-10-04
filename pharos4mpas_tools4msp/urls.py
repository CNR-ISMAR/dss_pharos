from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from apps.dss_pharos.urls import urlpatterns
from apps.dss_pharos import views


urlpatterns += [
#dss_pharos
#url(r'^.*$', include('apps.dss_pharos.urls')),  

#social
url(r"^accounts/", include("allauth.urls")),
url(r"^account/", include("allauth.urls")),
path('admin/', admin.site.urls),

path('help/', views.help, name='help'),

]
