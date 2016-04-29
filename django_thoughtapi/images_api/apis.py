from django.conf.urls import url
from . import api_views

urlpatterns = [
    url(r'$', api_views.root, name='root'),
]
