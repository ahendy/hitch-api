from django.shortcuts import render

from models import Ride
from rest_framework import viewsets
from serializer import RideSerializer
from rest_framework import generics
from HitchProject.Location.models import Location

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.



class RideViewSet(generics.ListCreateAPIView):
	def get_queryset(self):
		place_id = self.request.GET.get('place_id', '')
		if not place_id:
			return Ride.objects.all()
		else:
			try:
				print(place_id)
				location = Location.objects.get(place_id=place_id)
				print("got location")
				rides = Ride.objects.filter(destination=location).filter(passenger__isnull = True) # filter 
				return rides
			except:
				print("except")
				return []

	
	serializer_class = RideSerializer

class RideViewDetail(generics.RetrieveUpdateAPIView):
	queryset = Ride.objects.all()
	def get_serializer_class(self):
		return RideSerializer
	# serializer_class = RideSerializer 




