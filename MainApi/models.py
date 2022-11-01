# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import ugettext_lazy as _
import datetime
from .managers import CustomUserManager
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.


class user(AbstractUser):
	username = models.CharField(max_length=255, verbose_name='Username', unique=True)
	email = models.CharField(max_length=255, verbose_name='Staff ID', unique=True)
	id = models.AutoField(primary_key=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	GENDER_CHOICES = (('Male','Male'),('Female','Female'))
	objects = CustomUserManager()

	email = models.EmailField(_('Work Email'), null=True, blank=True, unique=True)
	firstname = models.CharField(max_length=255, verbose_name='First name')
	lastname = models.CharField(max_length=255, verbose_name='Last name')
	gender = models.CharField(choices=GENDER_CHOICES,default='Male', max_length=6)
	DOB = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
	mobile = PhoneNumberField(null=True, blank=True, verbose_name='Mobile Number')
	address = models.CharField(max_length=255,null=True, blank=True, verbose_name='Street Address')
	state = models.CharField(max_length=255,null=True, blank=True, verbose_name='State/Province')
	country = models.CharField(max_length=255, verbose_name='Country', default='Nigeria')
	profilePic = models.ImageField(upload_to='media/avatars', blank=True, null=True)


	def save(self, *args, **kwargs):
		force_update = False
		if self.id:
			force_update = True
		super(user, self).save(force_update=force_update)

	def __str__(self):
		return(self.username)