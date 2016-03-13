from django.shortcuts import render

from models import Ride
from rest_framework import viewsets
from serializer import RideSerializer
from rest_framework import generics
from HitchProject.Location.models import Location
from HitchProject.PersonApp.models import Person
from django.contrib.auth.models import User



from django.core.exceptions import ObjectDoesNotExist


# Create your views here.



class RideViewSet(generics.ListCreateAPIView):
	serializer_class = RideSerializer
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

#screw IT	

class RideViewDetail(generics.RetrieveUpdateAPIView):
	queryset = Ride.objects.all()
	def get_serializer_class(self):
		return RideSerializer
	# serializer_class = RideSerializer 
	
	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		print instance.passenger
		passengerpk = request.data.get("passenger")
		passengerobj = Person.objects.get( user = (User.objects.get(pk = passengerpk) )) 
		print passengerobj
		instance.passenger = passengerobj
		instance.save()
		serializer = RideSerializer(instance)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)



