from django.shortcuts import render_to_response, HttpResponse, render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings
from .models import *
from django.core.context_processors import csrf
from core.models import userP
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class registerU(TemplateView):
    template_name = 'registerU.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


    def post(self, request, *args, **kwargs):
        user = User(
            username=request.POST['inputusername'],
            first_name=request.POST['inputname'],
            last_name=request.POST['inpulastname'],
            email=request.POST['inputEmail'],
        )
        user.set_password(request.POST['inputpassword'],)
        user.save()
        usert=userP(
            user=user
        )
        usert.save()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))


class loginU(TemplateView):
    template_name = 'loginU.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        username = request.POST['inputusername']
        password = request.POST['inputpassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                render(request, '/proyectos_viviendas/lista', context_instance=RequestContext(request))
