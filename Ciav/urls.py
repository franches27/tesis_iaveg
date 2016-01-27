from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^ingenieros/', include('engineer.urls')),
    url('^proyectos_viviendas/', include('housing.urls')),
    url('^location/', include('Location.urls')),
    url('^user/', include('core.urls')),
]
