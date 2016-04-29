from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import api_views

urlpatterns = [
    url(r'$', api_views.root, name='root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
