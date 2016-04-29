from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'library/$', views.library_view, name='library'),
    url(r'albums/$', views.album_view, name='albums_view'),
    url(r'albums/(?P<album_id>\d+)$', views.album_view, name='album_view'),
    url(r'albums/add/$', views.album_add, name='album_add'),
    url(r'photos/$', views.photo_view, name='photos_view'),
    url(r'photos/(?P<photo_id>\d+)$', views.photo_view, name='photo_view'),
    url(r'photos/add/$', views.photo_add, name='photo_add'),

    url(r'profile/$', views.profile_view, name='self_view'),
    url(r'profile/(?P<profile_id>\d+)$', views.profile_view, name='profile_view'),
    # url(r'profile/edit/$', views.profile_edit, name='profile_edit'),
]
