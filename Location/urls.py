from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^parroquias/(?P<pk>[0-9]+)$', getParish, name='getParish'),
]
