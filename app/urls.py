from django.conf.urls import url
from django.conf.urls.static import static

from project import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # (r'^media/(?P</img>.*)$', 'django.views.static.serve',{'document_root': app/project/settings.MEDIA_ROOT})

static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]