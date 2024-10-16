from rest_framework import serializers
from .models import Hotel, Room, Bed

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'city', 'rating']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'price_per_bed', 'is_available']

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['room', 'bed_number', 'is_available']
