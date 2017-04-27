from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^api/', include('api.urls')),
]