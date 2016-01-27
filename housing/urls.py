from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^registro$', housingR.as_view(), name='registro'),	
	url(r'^lista$', housingL.as_view(), name='lista'),	
	url(r'^editar/(?P<slug>[0-9,a-z]+)$', housingU.as_view(), name='HousingU'),
	url(r'^vivienda/(?P<housing_slug>[0-9,a-z]+)$', getHousing, name='getHousing'),	
]
