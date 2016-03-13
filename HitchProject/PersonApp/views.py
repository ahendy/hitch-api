from django.shortcuts import render

from models import Person
from rest_framework import viewsets
from serializer import PersonSerializer
from rest_framework import generics
from rest_framework.response import Response

from HitchProject.Rides.serializer import RideSerializer


# Create your views here.



class PersonViewSet(generics.ListCreateAPIView):
	def get_queryset(self):	
		print "yo from herer"

		return Person.objects.all()
	serializer_class = PersonSerializer


class PersonViewDetail(generics.RetrieveUpdateAPIView):
	queryset = Person.objects.all()
	print queryset
	def get_serializer_class(self):
		return PersonSerializer
	
	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		print instance

# #		self.perform_update(serializer)
		return Response(PersonSerializer.data) #serializer.data)



class PersonViewHistory(generics.ListCreateAPIView):
	def get_queryset(self):
		one = self.request.GET.get('pk','')
		
		return Person.objects.all()
		#queryset = Rides.objects.all()
		

	serializer_class = PersonSerializer