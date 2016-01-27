from django.shortcuts import render_to_response, HttpResponse, render
from .models import *
import json

def getParish(request, pk):
	parroquia= parish.objects.filter(municipality=pk)
	dic={}
	lis=[]
	for x in parroquia:
		dic={}
		dic={
			"id": x.id,
			"name": x.name
		}
		lis.append(dic)
	result = json.dumps(lis, ensure_ascii=False)

	return HttpResponse(result, content_type='application/json; charset=utf-8')