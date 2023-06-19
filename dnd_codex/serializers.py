from rest_framework import serializers
from .models import Ally

class AllySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ally
        fields = ('id', 'name',)