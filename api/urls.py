from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^uid/(?P<uid>\w{32,32})$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
]