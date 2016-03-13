from django.shortcuts import render

from models import Ride
from rest_framework import viewsets
from serializer import RideSerializer
from rest_framework import generics
from HitchProject.Location.models import Location
from HitchProject.PersonApp.models import Person
from django.contrib.auth.models import User
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

class RideViewSet(generics.ListCreateAPIView):
	serializer_class = RideSerializer
	def get_queryset(self):
		place_id = self.request.GET.get('place_id', '')
		if not place_id:
			return Ride.objects.all()
		else:
			try:
				location = Location.objects.get(place_id=place_id)
				rides 	 = Ride.objects.filter(destination=location)				
				return rides
			except:
				print("exception on RideViewSet")
				return []


class RideViewDetail(generics.RetrieveUpdateAPIView):
	queryset = Ride.objects.all()
	def get_serializer_class(self):
		return RideSerializer
	# serializer_class = RideSerializer 
	
	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		print instance

		passengerpk  = request.data.get("passengers")[0]
		passengerobj = Person.objects.get(pk=passengerpk) 

		instance.passengers.add(passengerobj)
		serializer = RideSerializer(instance)
#		self.perform_update(serializer)
		return Response(serializer.data) #serializer.data)



