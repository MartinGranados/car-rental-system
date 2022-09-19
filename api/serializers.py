from dataclasses import fields
from rest_framework import serializers
from car_rental_system.models import Vehicle, Reservations

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'