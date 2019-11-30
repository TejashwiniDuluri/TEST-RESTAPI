from django.contrib.auth.models import User, Group

from rest_framework import serializers
from polls.models import *


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'account_type','password')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class FlightSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Flight
		fields = ('name','cat')
