# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import DataSerializer, UserSerializer
from .models import user
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from datetime import datetime
import json


class DataViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all().order_by('id')
	serializer_class = DataSerializer


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def getUser(request):
	token='null'
	token = request.META.get('HTTP_AUTHORIZATION')
	token = token[6:]
	try:
		Iuser = Token.objects.get(key=token).user
		serialized = UserSerializer(Iuser)
		return Response(serialized.data)
	except ObjectDoesNotExist:
		return Response('no')

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def updateUser(request):
	token='null'
	token = request.META.get('HTTP_AUTHORIZATION')
	token = token[6:]
	data = request.body
	data = json.loads(data)
	Iuser = Token.objects.get(key=token).user
	serialized = UserSerializer(instance = Iuser, data =data)
	if serialized.is_valid():
		serialized.save()
		return Response(serialized.data)
	else:
		return Response('no')
		
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@authentication_classes([])
@permission_classes([])
def CreateUser(request):
	data = request.body
	data = json.loads(data)
	date = data['date']
	date = datetime.strptime(date, '%Y-%m-%d').date()
	username = data['username']
	password = data['password']
	firstname = data['firstname']
	gender = data['gender']
	lastname= data['lastname']
	mobile = data['mobile']
	address = data['address']
	state = data['state']
	email = data['email']
	country = data['country']

	username = username.lower()
	try:
		newUser = user.objects.create_user(username=username,password=password)
		newUser.save()
		newUser.firstname=firstname
		newUser.lastname=lastname
		newUser.mobile = mobile
		newUser.email =email
		newUser.gender = gender
		newUser.DOB = date
		newUser.address=address
		newUser.state = state
		newUser.country = country
		newUser.save()
		ret = 'successful'
	except IntegrityError:
		ret = 'username'
	return Response(ret)

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
@authentication_classes([])
@permission_classes([])
def loginView(request,username,password):
	authUser = authenticate(username=username,password=password)
	if authUser is not None:
		if authUser.is_active:
			login(request._request,authUser)
			print(request.META.get('HTTP_AUTHORIZATION'))
			print(Token.objects.filter(user=authUser).first().key)
			ret = 'logged'
		else:
			ret ='inactive'
	else:
		ret = 'incorrect'
	return Response(ret)



@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def checkAuth(request):
	if request._request.user.is_authenticated:
		ret = 'logged'
		print (request._request.user)
	else:
		ret = 'no'
		print (request._request.user)
	return Response(ret)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def logoutView(request):
	logout(request._request)
	return Response('successful')