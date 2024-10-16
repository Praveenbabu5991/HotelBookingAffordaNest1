from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Hotel, Room, Bed
from .serializers import HotelSerializer, RoomSerializer, BedSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
