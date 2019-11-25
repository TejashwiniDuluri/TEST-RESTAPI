# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Flight(models.Model):
	name = models.CharField(max_length=200)
	cat = models.CharField(max_length=20)
	def __str__(self):
		return self.name