from models import Ride
from rest_framework import serializers


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('created_by', 'passenger','date', 'departure','destination')


