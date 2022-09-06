from rest_framework import serializers
from .models import *

class EventRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegister
        fields = ('id', 'Rollno', 'Name', 'Class', 'Age') 