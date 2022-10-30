# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import DataSerialzer
from .models import user
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class DataViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all().order_by('id')
	serializer_class = DataSerialzer
		
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def CreateUser(request,username,password,firstname,lastname,mobile,address,state,country):
	username = username.lower()
	try:
		newUser = user.objects.create_user(username=username,password=password)
		newUser.save()
		newUser.firstname=firstname
		newUser.lastname=lastname
		newUser.mobile = mobile
		newUser.address=address
		newUser.state = state
		newUser.country = country
		newUser.save()
		ret = 'successful'
	except:
		try:
			newUser.delete()
		except:
			pass
		ret = 'failed'
	return Response(ret)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def login(request,username,password):
	authUser = authenticate(username=username,password=password)
	if authUser is not None:
		if authUser.is_active:
			login(request._request, user,password)
			ret = 'logged'
		else:
			ret ='inactive'
	else:
		ret = 'incorrect'
	return Response(ret)



@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def checkAuth(request):
	if request.user.is_authenticated:
		ret = 'logged'
	else:
		ret = 'no'
	return Response(ret)

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def logoutView(request):
	logout(request._request)
	return Response('successful')