from django.conf.urls import include, url
from django.views.generic import TemplateView

from apps.dss_pharos import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^index$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^start$', views.sector_sel, name='dss_1'),
    url(r'^(?P<economic_sector_id>\d+)$', views.economic_sector_bg_info, name='economic_sector_bg_info'),
    url(r'^(?P<economic_sector_id>\d+)/ii$', views.economic_sector_interactions, name='economic_sector_interactions'),
    url(r'^(?P<economic_sector_id>\d+)/form$', views.economic_sector_form, name='economic_sector_form'),
    url(r'^(?P<usertype_id>\d+)/(?P<economic_sector_id>\d+)/result$', views.economic_sector_result, name='economic_sector_result'),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

