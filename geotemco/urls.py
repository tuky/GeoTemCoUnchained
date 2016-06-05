from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.geotemco),
    url(r'^(?P<name>.+)/$', views.data, name='geotemco_data_loader'),
]
