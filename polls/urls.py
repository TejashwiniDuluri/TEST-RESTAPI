from django.conf.urls import url,include

from django.contrib import admin
from django.conf import settings
from polls.views import *
from . import views


urlpatterns = [
	url(r'^demo/$',views.demo,name="demo"),
	url(r'^userslist/$',views.usersList.as_view({'get': 'list'})),
	url(r'^flightslist/$',views.AllFlights),
	url(r'^specificflight/(\d+)/$',views.specificFlight.as_view()),
	# url(r'^login$',views.login),

	# url(r'^flights/$',views.flights,name="flights"),




	]