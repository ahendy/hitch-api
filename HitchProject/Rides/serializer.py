from models import Ride
from rest_framework import serializers
from HitchProject.Location.serializer import LocationSerializer
from HitchProject.Location.models import Location


class RideSerializer(serializers.ModelSerializer):
	departure   = LocationSerializer()
	destination = LocationSerializer()
	passenger = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
	class Meta:
		model = Ride
		fields = ('created_by', 'passenger','date', 
					'departure','destination')

	def create(self, validated_data):
		departure = Location.objects.create(
			place_id = validated_data['departure']['place_id'],
			name = validated_data['departure']['name'],
		)
		destination = Location.objects.create(
			place_id = validated_data['destination']['place_id'],
			name = validated_data['destination']['name'],
		)	

		departure.save()
		destination.save()
		# person = Person.objects.get(user=self.request.user)

		ride = Ride.objects.create(
			departure		= departure,
			destination		= destination, 
			date 			= validated_data['date'],
			created_by		= validated_data['created_by']
			

		)
		ride.save()


		return ride
	# self.request.person