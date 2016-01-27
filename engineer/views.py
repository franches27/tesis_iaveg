from django.shortcuts import render_to_response, HttpResponse, render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings
from .models import *
from django.core.context_processors import csrf

# Create your views here.
class Index(TemplateView):
    template_name = 'eng_index.html'

    def get(self, request, *args, **kwargs):
    	is_post = False
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
    	is_post = True
    	try:
	    	ingeniero = engineer(
	    		name=request.POST['name'],
	    		lastname=request.POST['lastname'],
	    		ci=request.POST['cedula'],
	    		civ=request.POST['civ'],
	    		email=request.POST['email'],
	    		phone=request.POST['phone'],
	    		direction=request.POST['direcction'],
	    	)
	    	ingeniero.save()
	    	calse = 'success'
	    	message = "guardado exitoso"
    	except:
	    	calse = 'danger'
	    	message = "fallo al guardar"
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))