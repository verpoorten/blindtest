from django.conf.urls import url, include
from django.conf import settings
from . import views
from .models import *
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^encoding/([0-9]+)/$', views.result_encoding, name='result_encoding'),
    url(r'^save/([0-9]+)/$', views.save_result, name='save_result'),
    url(r'^home/([0-9]+)/$', views.change_tab_home, name='change_tab_home'),
    url(r'^tab/([0-9]+)/$', views.change_tab, name='change_tab'),
    url(r'^scores/([0-9]+)/$', views.view_scores, name='view_scores'),
    url(r'^encodings/([0-9]+)/$', views.results_encoding, name='results_encoding'),
    url(r'^gameset/save/results/$', views.save_results, name='save_results'),
    url(r'^play_display/all/([0-9]+)/$', views.display_player_all, name="display_player_all"),
    url(r'^play_display/gameset/([0-9]+)/$', views.results_view, name="results_view"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
