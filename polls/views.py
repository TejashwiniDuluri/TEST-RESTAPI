# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import serializers
# Create your views here.
from rest_framework import viewsets
from polls.serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

def demo(request):
	return  HttpResponse("done") 

class usersList(viewsets.ModelViewSet):
	permission_classes = IsAuthenticated
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def AllFlights(request):
	if request.method == 'GET':
		querysets = Flight.objects.all()
		serializer_class = FlightSerializer(querysets,many=True)
		return Response(serializer_class.data)

	if request.method == 'POST':
		# dataposted = JSONParser().parser(request)
		serializer = FlightSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

	if request.method == "DELETE":
		Flight.objects.all().delete()
		return HttpResponse("objects are deleted") 


# @api_view(['GET', 'POST','DELETE'])
class specificFlight(APIView):
	
	def get_object(self,id):
		try:
			objectrequired = Flight.objects.get(id=id)
			return objectrequired
		except objectrequired.DoesNotExist:
			return HttpResponse(status = status.HTTP_404_NOT_FOUND)

	def get(self,request,id,format=None):
		objectrequired = self.get_object(id)
		data = FlightSerializer(objectrequired)
		return Response(data.data)

	def put(self,request,id,format=None):
	
		objectrequired = self.get_object(id)
		serializer = FlightSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return JsonResponse(serializer.errors)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
# 	username=request.data.get("username")
# 	print(username)
# 	password=request.data.get("password")
# 	if username is None or password is None:
# 		return Response(status=HTTP_400_BAD_REQUEST)

# 	else:
# 		user = authenticate(username=username, password=password)
# 	if user == None:
# 		return Response(status=HTTP_404_NOT_FOUND)
# 	else:
# 		token = Token.objects.get(user=user)
# 		return Response({"token":token.key})
