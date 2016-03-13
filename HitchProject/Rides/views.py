from django.shortcuts import render

from models import Ride
from rest_framework import viewsets
from serializer import RideSerializer
from rest_framework import generics


# Create your views here.



class RideViewSet(generics.ListCreateAPIView):
	def get_queryset(self):
		return Ride.objects.all()
	
	serializer_class = RideSerializer




