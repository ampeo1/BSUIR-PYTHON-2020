from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^films/$', views.FilmListView.as_view(), name='films'),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'^producer/(?P<pk>\d+)$', views.ProducerDetailView.as_view(), name='producer-detail'),
    url(r'^producers/$', views.ProducerListView.as_view(), name='producers'),
    url(r'^film/create/$', views.FilmForm.as_view(), name='film-create'),
    url(r'^film/(?P<pk>\d+)/update/$', views.FilmUpdate.as_view(), name='film-update'),
    url(r'^film/(?P<pk>\d+)/delete/$', views.FilmDelete.as_view(), name='film-delete'),
    url(r'^producer/create/$', views.ProducerForm.as_view(), name='producer-create'),
    url(r'^producer/(?P<pk>\d+)/update/$', views.ProducerUpdate.as_view(), name='producer-update'),
    url(r'^producer/(?P<pk>\d+)/delete/$', views.ProducerDelete.as_view(), name='producer-delete'),
    url(r'^genre/create/$', views.GenreForm.as_view(), name='genre-create')
]
