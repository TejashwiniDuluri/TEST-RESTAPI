# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	def create_user(self,username,email,account_type,password,**kwargs):
		if not email:
			raise ValueError('Account must have a valid email address')
		user = self.model(
			username=username,
			email=email,
			password=password,
			account_type=account_type)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,username,email,password,**kwargs):
		user = self.model(username=username,email=email,password=password)         
		user.set_password(password)
		user.is_admin =True
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=200, null=True, blank=True,unique=True)
    email = models.EmailField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    account_types=(('student','student'),('teacher','teacher'))
    account_type = models.CharField(max_length=30,choices=account_types,null=True, blank=True)
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def get_short_name(self):
		return self.username

    def __str__(self):
    	return self.username




# Create your models here.
class Flight(models.Model):
	name = models.CharField(max_length=200)
	cat = models.CharField(max_length=20)
	def __str__(self):
		return self.name