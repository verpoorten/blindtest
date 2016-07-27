from django.conf.urls import url, include
from django.conf import settings
from . import views
from .models import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
