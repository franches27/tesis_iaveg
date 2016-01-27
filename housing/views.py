from django.shortcuts import render_to_response, HttpResponse, render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings
from .models import *
from django.core.context_processors import csrf
from Location.models import municipality
from engineer.models import engineer
import json


class housingR(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        municipio = municipality.objects.all().order_by('name')
        ingeniero = engineer.objects.all().order_by('name')
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        municipio = municipality.objects.all().order_by('name')
        ingeniero = engineer.objects.all().order_by('name')
        is_post = True
        try:

            vivienda = housing(
                id_o=request.POST['ido'],
                name=request.POST['name'],
                parish_id=request.POST['parroquia'],
                housing=request.POST['nviviendas'],
                description=request.POST['descripcion'],
                engineer_id=request.POST['ingeniero']
            )
            vivienda.save()
            calse = 'success'
            message = "guardado exitoso"
        except:
            calse = 'danger'
            message = "fallo al guardar"
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


class housingL(TemplateView):
    template_name = 'listaViv.html'

    def get(self, request, *args, **kwargs):
        viviendas=housing.objects.all().order_by('name')
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


class housingU(TemplateView):
    template_name = 'actualizarH.html'
    
    def get(self, request, slug, *args, **kwargs ):
        ingeniero = engineer.objects.all().order_by('name')
        municipio = municipality.objects.all().order_by('name')
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


def getHousing(request, housing_slug):
    parroquia= housing.objects.filter(slug=housing_slug)
    dic={}
    lis=[]
    for x in parroquia:
        dic={}
        dic={
            "id": x.id,
            "name": x.name,
            "parish": x.parish.name,
            "housing": x.housing,
            "description": x.description,
            "engineer_id": {"id": x.engineer.id,
                            "name": x.engineer.name},  
        }
        lis.append(dic)
    result = json.dumps(lis,indent=4, ensure_ascii=False)

    return HttpResponse(result, content_type='application/json; charset=utf-8')