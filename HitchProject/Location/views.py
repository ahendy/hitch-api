
from models import Location
from rest_framework import viewsets
from serializer import LocationSerializer
from rest_framework import generics


# Create your views here.



class LocationViewSet(generics.ListCreateAPIView):
	def get_queryset(self):
		return Location.objects.all()

	serializer_class = LocationSerializer


