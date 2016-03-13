from __future__ import unicode_literals
from HitchProject.PersonApp.models import Person
from django.db import models
from HitchProject.Location.models import Location

# Create your models here.


class Ride(models.Model):
	# created_by = models.OneToOneField(Person, related_name = 'usr1') #user1 != user2
	# created_by = models.ForeignKey(Person)
	passengers  = models.ManyToManyField(Person, blank = True,  null=True) 
	date        = models.DateField()
	time		= models.TimeField()
	departure 	= models.ForeignKey(Location, related_name = 'rides1',null=True)
	destination = models.ForeignKey(Location, related_name = 'rides2',null=True)
	

	# def __str__(self):
	# 	return self.departure, self.date
	# 	return '%s, %s, %s' % (departure.place_id, date, "" )