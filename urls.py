from django.conf.urls import url
from django.views.generic import TemplateView

from . import views



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^index$', TemplateView.as_view(template_name='dss_index.html'), name='dsshome'),
    url(r'^start$', views.level_1, name='dss_1'),
    url(r'^(?P<usertype_id>\d+)$', views.level_2, name='dss_2'),
    url(r'^(?P<usertype_id>\d+)/(?P<activity_id>\d+)$', views.activity_form, name='activity_form'),
    url(r'^(?P<usertype_id>\d+)/(?P<activity_id>\d+)/result$', views.activity_result, name='activity_result'),
]
