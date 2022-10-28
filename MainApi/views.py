# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, Response
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import DataSerialzer
from .models import user


class DataViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all().order_by('id')
	serializer_class = DataSerialzer
		

def CreateUser(request,username,password,firstname,lastname,mobile,address,state,country):
	newUser = user.objects.create_user(username=username,password=password)
	newUser.save()
	newUser.firstname=firstname
	newUser.lastname=lastname
	newUser.mobile = mobile
	newUser.address=address
	newUser.state = state
	newUser.country = country
	newUser.save()
	return HttpResponse("Successful")

def login(request,username,password):
	authUser = authenticate(username=username,password=password)
	if authUser is not None:
		if authUser.is_active:
			login(request, user,password)
			ret = 'logged'
		else:
			ret ='inactive'
	else:
		ret = 'incorrect'
	return Response(ret)