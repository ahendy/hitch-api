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


# Create your views here.



class RideViewSet(generics.ListCreateAPIView):
	serializer_class = RideSerializer
	def get_queryset(self):
		place_id = self.request.GET.get('place_id', '')
		if not place_id:
			return Ride.objects.all()
		else:
			try:
				#print(place_id)
				location = Location.objects.get(place_id=place_id)
				print(location)
				ride = Ride.objects.get(destination = location)
				print(ride)
				rloc = ride.destination.place_id
				print rloc
				rides = Ride.objects.filter(destination__place_id = rloc)
				#rides = Ride.objects.all()
				#rides = Ride.objects.filter(destination = location) # filter 
				#rides = Ride.objects.filter(destination = rloc)
				
				return rides
			except:
				print("except")
				return []


class RideViewDetail(generics.RetrieveUpdateAPIView):
	queryset = Ride.objects.all()
	def get_serializer_class(self):
		return RideSerializer
	# serializer_class = RideSerializer 
	
	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		print instance

		passengerpk = request.data.get("passengers")[0]
		print passengerpk
		passengerobj = Person.objects.get(pk=passengerpk) 
		print passengerobj
		instance.passengers.add(passengerobj)
		serializer = RideSerializer(instance)
#		self.perform_update(serializer)
		return Response(serializer.data) #serializer.data)



