from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.api_root, name='root'),
]
