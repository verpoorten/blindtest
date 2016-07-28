from django.conf.urls import url, include
from django.conf import settings
from . import views
from .models import *
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
