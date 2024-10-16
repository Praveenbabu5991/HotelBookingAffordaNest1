from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['guest', 'bed', 'check_in', 'check_out', 'includes_food', 'total_price']
