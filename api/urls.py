from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^uid/(?P<uid>\w{32,32})$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^chart/cars/uid/(?P<uid>\w{32,32})$', views.chartCars, name='chartCars'),
]