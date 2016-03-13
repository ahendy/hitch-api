from __future__ import unicode_literals
from HitchProject.Location.models import Location
from HitchProject.PersonApp.models import User
from django.db import models

# Create your models here.


class Ride(models.Model):
	created_by = models.OneToOneField(User, related_name = 'usr1') #user1 != user2
	passenger  = models.OneToOneField(User, related_name = 'usr2', blank = True,  null=True) 
	date       = models.DateField()
	
	departure 	= models.OneToOneField(Location, related_name = 'dep_loc')
	destination = models.OneToOneField(Location, related_name = 'dest_loc')

	def __str__(self):
		return '%s, %s, %s' % (self.created_by, self.passenger,self.pk )