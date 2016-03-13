from django.shortcuts import render

from models import Ride
from rest_framework import viewsets
from serializer import RideSerializer

# Create your views here.



class RideViewSet(viewsets.ModelViewSet):

	queryset = Ride.objects.all()
	serializer_class = RideSerializer
