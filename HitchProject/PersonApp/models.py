from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Person(models.Model): #Tweet table, contains attrib body, img_url, date
	
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	profile_pic = models.URLField()
	date 	= models.DateField()




