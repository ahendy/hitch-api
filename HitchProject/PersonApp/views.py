from django.shortcuts import render

from models import Person
from rest_framework import viewsets
from serializer import PersonSerializer
from rest_framework import generics


# Create your views here.



class PersonViewSet(generics.ListCreateAPIView):
	def get_queryset(self):
		print(Person.objects.all())
		return Person.objects.all()
	serializer_class = PersonSerializer
