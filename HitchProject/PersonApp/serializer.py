from models import Person
from rest_framework import serializers
from django.contrib.auth.models import User
import random

img_urls = [
			'http://factmag-images.s3.amazonaws.com/wp-content/uploads/2016/01/rtr_kanye_west_jc_150407_16x9_992.jpg',
			'http://static.stereogum.com/uploads/2015/03/Kanye-chain.jpg',
			'http://media1.popsugar-assets.com/files/2013/01/02/4/192/1922398/3df2ea52acfaf1ad_kan.xxxlarge_2.jpg',
			]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'first_name', 'last_name',
					'username', 'email', 'password')


class PersonSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Person
		fields = ('user', 'profile_pic', 'phone_num')

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
			user 		= user,
			profile_pic = img_urls[Random.seed()],
			phone_num 	= validated_data['phone_num']
		)
		person.save()
		# print("serializer")
		return person

