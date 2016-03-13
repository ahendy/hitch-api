from models import Person
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'first_name', 'last_name',
					'username', 'email', 'password')


class PersonSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Person
		fields = ('user', 'profile_pic','date', 'phone_num')

	def create(self, validated_data):
		user = User.objects.create(
			first_name 	= validated_data['user']['first_name'],
			last_name 	= validated_data['user']['last_name'],
			username 	= validated_data['user']['username'],
			email 		= validated_data['user']['email'],
		)

		user.set_password(validated_data['user']['password'])
		user.save()
		person = Person.objects.create(
			user = user,
			profile_pic = validated_data['profile_pic'],
			date 		= validated_data['date'],
			phone_num 	= validated_data['phone_num']
		)
		person.save()
		# print("serializer")
		return person