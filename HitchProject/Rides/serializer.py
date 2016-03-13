from models import Ride
from rest_framework import serializers
from HitchProject.Location.serializer import LocationSerializer
from HitchProject.Location.models import Location
from HitchProject.PersonApp.models import Person


class RideSerializer(serializers.ModelSerializer):
	departure   = LocationSerializer()
	destination = LocationSerializer()
	# passenger 	= serializers.PrimaryKeyRelatedField(required=False, read_only=True)
	
	class Meta:
		model  = Ride
		fields = ('pk', 'passengers','date', 'departure', 'destination',
					'time')

	def create(self, validated_data):
		temp_pid1 = validated_data['departure']['place_id']
		temp_pid2 = validated_data['destination']['place_id']
		
		try:
			departure = Location.objects.get(place_id = temp_pid1)
		except:
			departure 	= Location.objects.create(
				place_id 	= validated_data['departure']['place_id'],
				name 		= validated_data['departure']['name'],
			)
			departure.save()

		
		try:
			destination = Location.objects.get(place_id = temp_pid2)
		except:
			destination = Location.objects.create(
				place_id 	= validated_data['destination']['place_id'],
				name 		= validated_data['destination']['name'],
			)
			destination.save()
	

		# person = Person.objects.get(user=self.request.user)

		ride = Ride.objects.create(
			departure		= departure,
			destination		= destination, 
			date 			= validated_data['date'],
			# created_by		= validated_data['created_by'],
			time			= validated_data['time'],

		)
		ride.save()
		person = Person.objects.get(pk=validated_data['passengers'][0].pk)
		ride.passengers.add(person)
		return ride
	
	









