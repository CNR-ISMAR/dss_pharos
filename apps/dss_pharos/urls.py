from django.conf.urls import include, url
from django.views.generic import TemplateView

from apps.dss_pharos import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^index$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^start$', views.level_1, name='dss_1'),
    url(r'^(?P<usertype_id>\d+)$', views.level_2, name='dss_2'),
    url(r'^(?P<usertype_id>\d+)/(?P<activity_id>\d+)$', views.activity_bg_info, name='activity_bg_info'),
    url(r'^(?P<usertype_id>\d+)/(?P<activity_id>\d+)/form$', views.activity_form, name='activity_form'),
    url(r'^(?P<usertype_id>\d+)/(?P<activity_id>\d+)/result$', views.activity_result, name='activity_result'),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
