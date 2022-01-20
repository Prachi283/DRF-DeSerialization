from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def emp_create(request):
	if request.method=='POST':
		json_data= request.body
		stream= io.BytesIO(json_data)
		pythondata= JSONParser().parse(stream)
		serializer= EmpSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res={'msg':'Data is created'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer.render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json')
