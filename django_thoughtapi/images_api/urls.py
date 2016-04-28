from django.conf.urls import url
from . import views

url_patterns = [
    url(r'library/$', views.library_view, name='library'),
    url(r'albums/$', views.album_view, name='albums_view'),
    url(r'albums/(?P<album_id>\d+)$', views.album_view, name='album_view'),
    url(r'albums/add/$', views.album_add, name='album_add'),
    url(r'photos/$', views.photo_view, name='photos_view'),
    url(r'photos/(?P<photo_id>\d+)$', views.photo_view, name='photo_view'),
    url(r'photos/add/$', views.photo_add, name='photo_add'),
]
