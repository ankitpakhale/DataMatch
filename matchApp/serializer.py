from pyexpat import model
from turtle import mode
from .models import *
from rest_framework import serializers


class Uploadcsvserializer(serializers.Serializer):
    file = serializers.FileField()
    
    class Meta:
        fields = ('file')

class Uploadcsvserializer1(serializers.ModelSerializer):
    class Meta:
        model = Uploadcsv
        fields = '__all__'


 