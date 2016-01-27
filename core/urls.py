from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^register$', registerU.as_view(), name='registerU'),
	url(r'^login$', loginU.as_view(), name='loginU'),
]
