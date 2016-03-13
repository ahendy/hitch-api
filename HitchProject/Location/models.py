from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Location(models.Model): #Tweet table, contains attrib body, img_url, date
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	longi = models.DecimalField(max_digits=9, decimal_places=6)

	addr = models.CharField(max_length=70)
	StateProv = models.CharField(max_length = 70)
	zipCode =  models.CharField(max_length = 7)






