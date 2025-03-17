from django.shortcuts import render

from rest_framework import generics

from .serializers import CarSerializer
from .models import Car

# Create your views here.

class CarListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
    
class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()