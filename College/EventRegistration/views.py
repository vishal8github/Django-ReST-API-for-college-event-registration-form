from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


#CRUD operations

class ListEventRegister(generics.ListAPIView):
    queryset = EventRegister.objects.all()
    serializer_class = EventRegisterSerializer

class DetailEventRegister(generics.RetrieveUpdateAPIView):
    queryset = EventRegister.objects.all()
    serializer_class = EventRegisterSerializer

class CreateEventRegister(generics.CreateAPIView):
    queryset = EventRegister.objects.all()
    serializer_class = EventRegisterSerializer

class UpdateEventRegister(generics.UpdateAPIView):
    queryset = EventRegister.objects.all()
    serializer_class = EventRegisterSerializer

class DeleteEventRegister(generics.DestroyAPIView):
    queryset = EventRegister.objects.all()
    serializer_class = EventRegisterSerializer