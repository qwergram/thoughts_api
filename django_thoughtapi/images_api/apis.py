from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import api_views

urlpatterns = [
    url(r'album/$', api_views.album, name='album'),
    url(r'photo/$', api_views.photo, name='photo'),
    url(r'$', api_views.root, name='root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
