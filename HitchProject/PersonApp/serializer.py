from models import Person
from rest_framework import serializers
from django.contrib.auth.models import User



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('user', 'profile_pic','date')


    # def create(self, validated_data):
    #  	user = User.objects.create(
    #  		first_name = validated_data['first_name']
    #  		last_name  = validated_data['last_name']
    #  		username   = validated_data['username']
    #  		email 	   = validated_data['email']
    #  	)
    #  	user.set_password(validated_data['password'])
    #  	user.save()

    #  	person = Person.objects.create(
    #  		user = user
    #  		profile_pic = validated_data['img']
    #  		date 		= validated_data['date']
    #   		)

    #  	person.save()
    #  	return person